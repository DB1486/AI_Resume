from pymongo import MongoClient
from backend.config import MONGO_URL, DB_NAME
client = MongoClient(MONGO_URL)
db = client[DB_NAME]

resumes_collection = db["resumes"]
jobs_collection = db["jobs"]