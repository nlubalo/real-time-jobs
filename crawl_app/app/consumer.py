from db import DatabaseConnection
from pymongo import MongoClient
import os
from kafka import KafkaConsumer
import json

def create_database(url, db_name, table_name):
    client = MongoClient(url)
    dbname = client[db_name]
    collection_name = dbname[table_name]
    print(collection_name)

    return collection_name


create_database('mongodb://mongodb:27017', "crawl_jobs", "tech_jobs")


def insert_data(url, data):
    client = MongoClient(url)
    collection_name = client.crawl_jobs.tech_jobs
    collection_name.insert_one(data)


def kafka_consume(topic_name):
    consumer = KafkaConsumer(
        topic_name,
        auto_offset_reset="earliest",
        bootstrap_servers=["kafka:9091"],
        api_version=(0, 10),
        consumer_timeout_ms=1000,
    )
    return consumer

consumer_data = kafka_consume('tech-jobs')
for msg in consumer_data:
    html = msg.value
    out = json.loads(html.decode('unicode_escape'))
    insert_data('mongodb://mongodb:27017', out)