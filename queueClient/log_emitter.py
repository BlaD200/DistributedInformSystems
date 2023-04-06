import pika
import datetime

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Info or Debug
log_type = input('Log type: ')
log_hash = input('Log hash: ')
log_message = input('Log message: ')
log_date = str(datetime.datetime.now())

message_body = '{"hashValue": "%s", "message": "%s", "timestamp": "%s"}' % (log_hash, log_message, log_date)

exchange_name = 'LogProcessingExchange'

channel.exchange_declare(exchange='LogProcessingExchange', exchange_type='direct')

routing_key = 'processLog' + log_type


channel.basic_publish(
    exchange='LogProcessingExchange', routing_key=routing_key, body=message_body)
print(" Sent %s:%s" % (routing_key, message_body))
connection.close()
