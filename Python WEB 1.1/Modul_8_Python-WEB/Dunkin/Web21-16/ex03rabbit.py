import pika
import sys

from ex02rabbit import URL


def main():
    # credentials = pika.PlainCredentials('guest', 'guest')
    # connection = pika.BlockingConnection(
    #     pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    connection = pika.BlockingConnection(pika.URLParameters(URL))
    channel = connection.channel(channel_number=1)

    channel.queue_declare(queue='hello_world')

    def callback(*args):
        print(f" [x] Received {args[3]}")
        

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='hello_world', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)