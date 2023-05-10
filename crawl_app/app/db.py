import os
from contextlib import contextmanager
from pymongo import MongoClient


class DatabaseConnection:
    def __init__(self, url):
        self.conn_url = url

    @contextmanager
    def managed_cursor(self):
        self.conn = MongoClient(self.conn_url)
        try:
            yield self.conn
        finally:
            self.conn.close()


def get_warehouse_credentials():
    return (os.getenv("MONGODB_URL", ""),)
