import pymongo

fetcher = pymongo.MongoClient("mongodb+srv://techcommittee:SmvuOBEJSrSdQGrf@surveycluster.a2fw86w.mongodb.net/stuco-surveys?retryWrites=true&w=majority")

db = fetcher["survey-responses"]

