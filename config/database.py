from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:Onosediafo_1@cluster0.6x0a4cc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client.todo_db

collection_name = db['todo_collection']
