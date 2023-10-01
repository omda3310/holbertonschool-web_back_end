#!/usr/bin/env python3
"""A Python script that provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient
Methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]


if __name__ == "__main__":
    """Connect to database"""
    clt = MongoClient('mongodb://127.0.0.1:27017')
    n_collection = clt.logs.nginx
    number_logs = n_collection.count_documents({})
    print("{} logs".format(number_logs))
    print("Methods:")
    for method in Methods:
        if method == None:
            print("\tmethod GET: 0")
            print("\tmethod POST: 0")
            print("\tmethod PUT: 0")
            print("\tmethod PATCH: 0")
            print("\tmethod DELETE: 0")
            print("0 status check")
        number_logs = n_collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, number_logs))
    cheked_status = n_collection.count_documents({"method": "GET", "path": "/status"})
    print("{} status check".format(cheked_status))
