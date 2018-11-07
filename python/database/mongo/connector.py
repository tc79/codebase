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


def connect_to_database(uri="mongodb://localhost", database="db"):
    client = MongoClient(uri, serverSelectionTimeoutMS=1000)
    db = client.database
    try:
        # Send a query to the server to see if the connection is working.
        db.list_collections()
    except Exception:
        raise
    return db
