import os
import sys
import json
from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")

import certifi
ca = certifi.where()

import pandas as pd
import pymongo
from networksecurity.logging.logger import logging  # Ensure this is a logger instance
from networksecurity.exception.exception import NetworkSecurityException

class NetworkDataExtract:

    def __init__(self):
        pass

    def csv_to_json_converter(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def insert_data_mongodb(self, records, database, collection):
        try:
            mongo_client = pymongo.MongoClient(MONGO_DB_URL, tlsCAFile=ca)
            db = mongo_client[database]
            coll = db[collection]
            coll.insert_many(records)
            mongo_client.close()
            return len(records)
        except Exception as e:
            raise NetworkSecurityException(e, sys)

if __name__ == '__main__':
    FILE_PATH = "Network_Data/phisingData.csv"
    DATABASE = "ADDYDB"
    COLLECTION = "Network Data"
    network_obj = NetworkDataExtract()
    records = network_obj.csv_to_json_converter(file_path=FILE_PATH)
    print(records)
    no_of_records = network_obj.insert_data_mongodb(records, DATABASE, COLLECTION)
    print(no_of_records)
