# from ..core.database import client
from pymongo import MongoClient
from requests import delete

# client = MongoClient("localhost", 27017)

client = MongoClient("mongodb://localhost:27017")

class CRUDMongo:
    def __init__(self) -> None:
        self.collection = None

    def select_db(self):
        db = client["test"]
        users_col = db["users"]
        self.collection = users_col

    def create(self, data):
        self.collection.insert_one(data)

    def read(self, name=None, surname=None, age=None, profession=None):
        entity = self.collection.find_one({"name": name})

    def update(self, name=None, surname=None, age=None, profession=None):
        self.collection.update_one({"name": name}, {"$set": {"name": "John", "age": age}})

    def delete(self, name=None, surname=None, age=None, profession=None):
        self.collection.delete_one({"name": "Amil"})

    def call(self):
        self.select_db()
        data = {
                "name": "Amil",
                "surname": "Alizada",
                "age": 24,
                "profession": "Developer"
            }
        self.create(data)
        self.read(name="Amil")
        self.update(name="Amil", age=28)
        self.delete(name="Amil")


instance = CRUDMongo().call()