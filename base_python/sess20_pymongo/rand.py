from pymongo import MongoClient

connection_uri = "mongodb+srv://mark_db_user:Mark123@cluster0.ymuke3q.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(connection_uri)

db = client["sample_airbnb"]

collection = db["listingsAndReviews"]

print("Databases:", client.list_database_names())
