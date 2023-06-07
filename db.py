import os

from pymongo import MongoClient


class Db:
    def __init__(self):
        self.client = MongoClient(os.environ['CS_MONGODB'])

    def check_availability(self):
        return 'Softwares' in self.client.list_database_names()
