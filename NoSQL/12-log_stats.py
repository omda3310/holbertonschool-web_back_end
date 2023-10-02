#!/usr/bin/env python3
"""A Python script that provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient
Methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def status_log(n_collection, var=None):
    """a Python script that provides some stats about Nginx logs stored in MongoDB"""
    if var:
        number_logs = n_collection.count_documents({"method": var})
        print(f'\tmethod {var}: {number_logs}')
        return
    number_logs = n_collection.count_documents({})
    print(f'{number_logs} logs')
    print("Methods:")
    for method in Methods:
        number_logs = n_collection.count_documents({"method": method})
        print(f'\tmethod {method}: {number_logs}')
    cheked_status = n_collection.count_documents({"method": "GET", "path": "/status"})
    print(f'{cheked_status} status check')
    
    
    if __name__ == "__main__":
        """Connect to database"""
        clt = MongoClient('mongodb://127.0.0.1:27017')
        n_collection = clt.logs.nginx
        status_log(n_collection)
