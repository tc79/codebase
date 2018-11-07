# https://docs.mongodb.com/manual/reference/sql-comparison/
from pymongo import MongoClient


def connect(uri="mongodb://localhost"):
    client = MongoClient(uri, serverSelectionTimeoutMS=1000)

    # Send a query to the server to see if the connection is working.
    try:
        client.server_info()
    except Exception:
        raise
    return client

