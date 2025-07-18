from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URL")
DATABASE_NAME = os.getenv("MONGO_DB", "group_routing_database")

client = MongoClient(MONGO_URI)

def get_database():
    try:
        client.admin.command("ping")
        print("✅ MongoDB connection successful.")
        db = client[DATABASE_NAME]
        return db
    except ConnectionFailure as e:
        print(f"❌ Could not connect to MongoDB: {e}")
        return None
