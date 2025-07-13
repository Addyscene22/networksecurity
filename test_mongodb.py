from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
DATABASE_NAME = "ADDYDB"
COLLECTION_NAME = "Network Data"

try:
    client = MongoClient(MONGO_DB_URL)
    db = client[DATABASE_NAME]
    collection = db[COLLECTION_NAME]
    count = collection.count_documents({})
    print(f"✅ Successfully connected. Found {count} documents in collection '{COLLECTION_NAME}'.")
except Exception as e:
    print(f"❌ Connection failed: {e}")
