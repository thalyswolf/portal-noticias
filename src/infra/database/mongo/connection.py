from pymongo import MongoClient
from dotenv import load_dotenv
import os


class MongoConnection:
    _instance = None
    _client = None


    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)

        return cls._instance


    def __init__(self):
        if self._client is None:
            load_dotenv()
            CONNECTION_STRING = str(os.environ.get('MONGO_CONNECTION'))
            self._client = MongoClient(CONNECTION_STRING)
            

    def get_database(self):
        return self._client['teste']


    def get_client(self):
        return self._client
