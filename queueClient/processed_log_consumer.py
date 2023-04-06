import pika


connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

exchange_name = "LogProcessedExchange"

channel.exchange_declare(exchange=exchange_name, exchange_type='direct', durable=True)

queue_name = "LogProcessedQueue"

result = channel.queue_declare(queue=queue_name, durable=True)


channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key='processedLog')

print('Waiting for processed logs. To exit press Ctrl+C')


def callback(ch, method, properties, body):
    print(" [log] %s:%s" % (method.routing_key, body))


channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()
