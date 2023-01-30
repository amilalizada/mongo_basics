import pymongo
from pymongo import MongoClient

# client = MongoClient("localhost", 27017)

client = MongoClient("mongodb://localhost:27017")

class FindAndCursor:

    def __init__(self):
        self.collection = None

    def select_db(self):
        db = client["test"]
        users_col = db["users"]
        self.collection = users_col

    def find(self):
        cursor_users = self.collection.find({"name": "Amil"})
        for data in cursor_users:
            print(data)
        print(cursor_users.alive)

    def sort(self):
        #also we can use ASCENDING
        for document in self.collection.find({}).sort("age", pymongo.DESCENDING):
            print(document)

        for document in self.collection.find({}).sort([("age", pymongo.DESCENDING), ("name", pymongo.DESCENDING)]):
            print(document)

    def limit(self):
        # Or we can use SKIP instead of limit
        documents = self.collection.find({}).limit(5)
        print(documents)

    def count(self):
        query_filter = {"name": "Amil"}
        count = self.collection.count_documents(query_filter)
        print(count)

    def distinct(self):
        users_cursor = self.collection.find({})
        users_cursor.distinct("name")

    def call(self):
        self.select_db()
        self.find()
        self.sort()
        self.count()
        self.distinct()


isntance = FindAndCursor().call()