import pymongo
from pymongo import MongoClient;
from dotenv import load_dotenv
import os

load_dotenv()

fetcher = pymongo.MongoClient(os.environ.get("stuco_mongo_db"))
print(fetcher.list_database_names())

db = fetcher['stuco-surveys']
data = db['survey-responses']

# Accessing the dorm events survey
last_response = data.find_one({'surveyId': "ObjectId('65b82a97a569b1676101eab0')"})
print(last_response)

