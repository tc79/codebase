def insert_document(database, collection_name, document):
    try:
        id = database.collection_name.insert_one(document).inserted_id
    except Exception:
        raise
    return id
