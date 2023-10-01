#!/usr/bin/env python3
"""A Python script that provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient
Methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]


if __name__ == "__main__":
    """Connect to database"""
    clt = MongoClient("mongodb://127.0.0.1:27017")
    n_collection = clt.logs.nginx
    number_logs = n_collection.count_documents({})
    print("{} logs".format(number_logs))
    print("Methods:")
    for method in Methods:
        number_logs = n_collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, number_logs))
    cheked_status = n_collection.count_documents({"method": "GET", "path": "/status"})
    print("{ status check}".format(cheked_status))

    



