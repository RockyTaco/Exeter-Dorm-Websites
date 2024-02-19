import pymongo
from dotenv import load_dotenv
import os

load_dotenv()

fetcher = pymongo.MongoClient(os.environ.get("stuco_mongo_db"))

db = fetcher["survey-responses"]

