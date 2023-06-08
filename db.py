import os

from bson import ObjectId
from pymongo import MongoClient


CS_ENV = 'CS_MONGODB'
DB_NAME = 'Softwares'
COL_NAME = 'Keys'

class Db:
    def __init__(self):
        self.client = MongoClient(os.environ[CS_ENV])
        self.db = self.client[DB_NAME]
        self.col = self.db[COL_NAME]

    def initialize(self):
        self.col.insert_one({})

    def db_col_is_available(self):
        return DB_NAME in self.client.list_database_names() and COL_NAME in self.db.list_collection_names()

    def get_all_softwares(self):
        return self.col.find()

    def insert_software(self, name, producer):
        self.col.insert_one({'name': name, 'producer': producer, 'keys': []})

    def get_software(self, serial):
        return self.col.find_one({'_id': ObjectId(serial)})

    def insert_key(self, software, key):
        return self.col.update_one({'_id': software['_id']}, {'$push': {'keys': key}})
