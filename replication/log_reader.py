from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger
from mysql import connector

severities = ['Info', 'Debug']

scheduler = BlockingScheduler()
last_record = 0
readDB = connector.connect(db='mydata', host="127.0.0.1", port=33062, user="root", password="mysql2pass")


@scheduler.scheduled_job(IntervalTrigger(seconds=2))
def read_message():
    global last_record
    sql_select_Query = "select * from logs LIMIT %s, %s" % (last_record, last_record + 10)
    print(sql_select_Query)
    cursor = readDB.cursor()
    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()
    last_record += cursor.rowcount
    print("Total number of rows in table: ", last_record)

    print("\nPrinting each row")
    for row in records:
        print("Id = ", row[0], )
        print("Message = ", row[1])
        print("Date  = ", row[2])
        print()


if __name__ == '__main__':
    print(readDB)
    scheduler.start()
