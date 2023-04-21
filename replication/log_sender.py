import datetime
import random

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger
from mysql import connector

severities = ['Info', 'Debug']

scheduler = BlockingScheduler()

writeDB = connector.connect(db='mydata', host="127.0.0.1", port=33061, user="root", password="mysql1pass")


def generate_message():
    log_hash = str(random.getrandbits(128))
    random_string = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=5))
    log_message = f'{random_string} is a random string pretending to be a log'
    log_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return log_hash, log_message, log_date


@scheduler.scheduled_job(IntervalTrigger(seconds=2))
def send_message():
    log_type = random.choice(severities)
    log_hash, log_message, log_date = generate_message()

    mySql_insert_query = """INSERT INTO logs (id, log_mesage, log_date) 
                           VALUES 
                           ('%s', '%s', '%s');""" % (log_hash, log_message, log_date)
    print(mySql_insert_query)
    cursor = writeDB.cursor()
    cursor.execute(mySql_insert_query)
    writeDB.commit()
    cursor.close()

    print("Wrote %s:%s" % (log_type, log_message))


if __name__ == '__main__':
    print(writeDB)
    scheduler.start()
