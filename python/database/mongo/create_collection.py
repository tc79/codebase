def create_collection(database, collection_name, drop_if_exists=True):
    if drop_if_exists and collection_name in database.list_collections():
        database.drop_collection(collection_name)
    return database.collection_name
