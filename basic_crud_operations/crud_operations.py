import pymongo
from pymongo import MongoClient
from pymongo import collection

# cluster = MongoClient("mongodb+srv://<username>:<password>@cluster0.lawgn.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# 1) username
# 2) password
# 3) myFirstDatabase

cluster = MongoClient("mongodb+srv://prashanth:abc_123@cluster1.swuik.mongodb.net/database_1?retryWrites=true&w=majority")

db = cluster['database_1']         ## going from client to data-base
collection = db['collection_1']    ## going from data-base to collections

documents = { "_id":4, "name":"Sabarinathan", "score":100 }

collection.insert_one(documents)



