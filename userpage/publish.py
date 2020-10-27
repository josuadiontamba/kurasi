import pika 
import os


def sentviabroker(msg):
  url = os.environ.get('CLOUDAMQP_URL', 'amqps://ykzquwhx:g1fOkQt549xpZZny9egs3KXWF_epr-vi@coyote.rmq.cloudamqp.com/ykzquwhx')
  params = pika.URLParameters(url)
  connection = pika.BlockingConnection(params)
  channel = connection.channel()
  channel.queue_declare(queue='task_queue', durable=True)
  # message = ' '.join(sys.argv[1:]) or "Hello World!"
  message = msg
  # message = "test 123"
  channel.basic_publish(
      exchange='',
      routing_key='task_queue',
      body=message,
      properties=pika.BasicProperties(
          delivery_mode=2,  # make message persistent
      ))
  print(" [x] Sent %r" % message)
  connection.close()
  

def sentviabroker2(msg):
  # Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
  url = os.environ.get('CLOUDAMQP_URL', 'amqps://oxplckge:brEVA_doZ02gf0xzmn8YtfctPoJauZZ6@finch.rmq.cloudamqp.com/oxplckge')
  # amqps://oxplckge:brEVA_doZ02gf0xzmn8YtfctPoJauZZ6@finch.rmq.cloudamqp.com/oxplckge
  params = pika.URLParameters(url)
  connection = pika.BlockingConnection(params)
  channel = connection.channel() # start a channel
  channel.queue_declare(queue='hello') # Declare a queue
  channel.basic_publish(exchange='',
                        routing_key='hello',
                        body=msg)

  print(" [x] Sent to broker")
  connection.close()