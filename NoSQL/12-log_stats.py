#!/usr/bin/env python3
"""A Python script that provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


if __name__ == '__main__':
    """Connect to database"""
    clt = MongoClient()
    nginx_collection = clt.logs.nginx
    """a Python script that provides some stats about Nginx logs stored in MongoDB"""
    number_logs = nginx_collection.count_documents({})
    print(f'{number_logs} logs')

    Methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in Methods:
        number_logs_method = nginx_collection.count_documents({"method": method})
        print(f'\tmethod {method}: {number_logs_method}')

    cheked_status = nginx_collection.count_documents({"method": "GET", "path": "/status"})
    print(f'{cheked_status} status check') 
