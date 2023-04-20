import pika
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger
import datetime
import random


severities = ['Info', 'Debug']

exchange_name = 'LogProcessingExchange'

scheduler = BlockingScheduler()


def generate_message():
    log_hash = str(random.getrandbits(128))
    random_string = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=5))
    log_message = f'{random_string} is a random string pretending to be a log'
    log_date = str(datetime.datetime.now())
    message_body = '{"hashValue": "%s", "message": "%s", "timestamp": "%s"}' % (log_hash, log_message, log_date)
    return message_body


@scheduler.scheduled_job(IntervalTrigger(seconds=2))
def send_message():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    log_type = random.choice(severities)

    message_body = generate_message()

    channel.exchange_declare(exchange='LogProcessingExchange', exchange_type='direct', durable=True)

    routing_key = 'processLog' + log_type

    channel.basic_publish(
        exchange='LogProcessingExchange', routing_key=routing_key, body=message_body)
    print(" Sent %s:%s" % (routing_key, message_body))
    connection.close()


if __name__ == '__main__':
    scheduler.start()

