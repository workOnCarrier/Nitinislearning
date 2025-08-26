from kafka import KafkaConsumer

server = 'kafka-broker'
port = '29092'
topic = 'kafka.learning.orders_2'

def main():
    # Create a Kafka consumer
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=f'{server}:{port}',
        group_id='kafka-python-consumer',
        auto_offset_reset='earliest',
        key_deserializer=lambda k: k.decode('utf-8') if k else None,
        value_deserializer=lambda v: v.decode('utf-8') if v else None
    )

    # Continuously poll for new messages
    for message in consumer:
        print(f"Message fetched : {message}")

if __name__ == "__main__":
    main()