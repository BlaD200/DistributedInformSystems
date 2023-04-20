import pika

exchange_name = "LogProcessedExchange"

queue_name = "LogProcessedQueue"


def callback(ch, method, properties, body):
    print(" [log] %s:%s" % (method.routing_key, body.decode()))


def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange=exchange_name, exchange_type='direct', durable=True)

    result = channel.queue_declare(queue=queue_name, durable=True)

    channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key='processedLog')

    channel.basic_consume(
        queue=queue_name, on_message_callback=callback, auto_ack=True)

    print('Waiting for processed logs. To exit press Ctrl+C')

    channel.start_consuming()


if __name__ == '__main__':
    main()
