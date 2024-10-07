from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['your_db_name']

# Example usage: db.users.insert_one({"name": "John Doe"})
