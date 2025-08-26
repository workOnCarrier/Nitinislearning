from kafka import KafkaProducer
import random
import time

server = 'kafka-broker'
port = '29092'
topic = 'kafka.learning.orders_2'

def main():
    # Create a Kafka producer
    producer = KafkaProducer(
        bootstrap_servers=f'{server}:{port}',
        key_serializer=lambda k: k.encode('utf-8'),
        value_serializer=lambda v: v.encode('utf-8')
    )

    # Publish 10 messages at 2 second intervals, with a random key
    start_key = random.randint(0, 999)
    try:
        for i in range(start_key, start_key + 10):
            key = str(i)
            value = f"This is order : {i}"
            print(f"Sending Message : topic={topic}, key={key}, value={value}")
            producer.send(f'{topic}', key=key, value=value)
            time.sleep(2)
    finally:
        producer.close()

if __name__ == "__main__":
    main()