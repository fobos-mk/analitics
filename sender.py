import pika
import json
import sys, os


def responce(ResponceData, hostname, ResponceQueue):
    creditional = pika.PlainCredentials(username='admin', password='admin')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=hostname, port=5672, credentials=creditional))
    channel = connection.channel()
    channel.queue_declare(queue=ResponceQueue)
    channel.basic_publish(exchange='', routing_key=ResponceQueue, body=json.dumps(ResponceData))
    # print(f"Sent {responce_data}")
    connection.close()


if __name__ == '__main__':
    try:
        responce()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
