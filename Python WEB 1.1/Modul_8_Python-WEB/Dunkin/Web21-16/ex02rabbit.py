import pika

URL = "<YOU_URL>"

def main():
    # credentials = pika.PlainCredentials('guest', 'guest')
    # connection = pika.BlockingConnection(
    #     pika.ConnectionParameters(
    #         host='localhost', 
    #         port=5672, 
    #         credentials=credentials
    #         )
    #     )
    connection = pika.BlockingConnection(pika.URLParameters(URL))
    channel = connection.channel()

    channel.queue_declare(queue='hello_world')

    channel.basic_publish(
        exchange='',
        routing_key='hello_world', 
        body='Hello world!'.encode()
        )
    # channel.basic_publish(exchange='', routing_key='hello_world', body='Hello world! There'.encode())
    print(" [x] Sent 'Hello World!'")
    connection.close()


if __name__ == '__main__':
    main()
