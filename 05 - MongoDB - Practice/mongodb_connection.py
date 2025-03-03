from pymongo import MongoClient
from dotenv import load_dotenv
import os


class MongoDB_Connection:
    # db_name : str
    # collection_name : str
    # cluster_uri : str
    # collection : Collection

    def __init__(
        self,
        db_name: str = None,
        collection_name: str = None,
        cluster_uri: str = None,
    ) -> None:
        self.db_name = db_name
        self.collection_name = collection_name
        self.cluster_uri = cluster_uri
        if not self.cluster_uri:
            self.set_cluster_uri_by_env()


    def set_cluster_uri(self, cluster_uri: str) -> None:
        self.cluster_uri = cluster_uri

    def set_cluster_uri_by_env(self, env_route: str = None) -> None:
        load_dotenv(env_route)
        self.cluster_uri = os.getenv("CLUSTER_URI") or input(
            ".env CLUSTER_URI empty, please insert the cluster uri:\n"
        )

    def set_db_name(self, db_name: str) -> None:
        self.db_name = db_name

    def set_collection_name(self, collection_name: str) -> None:
        self.collection_name = collection_name


    def connect(self):

        if not self.cluster_uri:
            self.set_cluster_uri(input("Please, insert the cluster uri:\n"))
        if not self.db_name:
            self.set_db_name(input("Please, insert the database name:\n"))
        if not self.collection_name:
            self.set_collection_name(input("Please, insert the collection name:\n"))

        client = MongoClient(self.cluster_uri)
        db = client[self.db_name]
        collection = db[self.collection_name]
        self.collection = collection
        return collection
