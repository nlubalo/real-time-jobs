import json
from kafka import KafkaConsumer, KafkaProducer
from scrape_jobs import get_tech_jobs


def connect_kafka_producer():
    producer = None
    try:
        producer = KafkaProducer(
            bootstrap_servers=["kafka:19091"],  # localhost:9091
            value_serializer=lambda m: json.dumps(m).encode("ascii"),
        )
    except Exception as e:
        print("Exception while connecting Kafka")
        print(str(e))
    finally:
        return producer


def publish_message(message, topic):
    try:
        producer = connect_kafka_producer()
        producer.send(topic, message)
        producer.flush()

    except Exception as e:
        print("Exception while publishing data")
        print(str(e))


if __name__ == "__main__":
    jobs = get_tech_jobs()
    for job in jobs:
        print(job)
        publish_message(job, "tech-jobs")
