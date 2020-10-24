# -*- coding: utf-8 -*-
"""
测试如何使用python的pymongo模块操作MongoDB

@author: hch
@date  : 2020/10/8
"""
import logging
import time
import traceback
from pprint import pprint

from pymongo import MongoClient
from pymongo.cursor import Cursor
from pymongo.results import DeleteResult, InsertOneResult, UpdateResult


class MongoTest:
    client = None

    try:
        client = MongoClient('mongodb://root:root@localhost:27017/test?authSource=admin')
        print('init mongo client:', client)
    except Exception as e:
        # traceback.print_exc()
        logging.exception(e)

    @classmethod
    def get_connection(cls) -> MongoClient:
        return cls.client or MongoClient('mongodb://root:root@localhost:27017/test?authSource=admin')

    @classmethod
    def insert(cls, db: str, collection: str, data: dict) -> InsertOneResult:
        return cls.client.get_database(db).get_collection(collection).insert_one(data)

    @classmethod
    def find(cls, db: str, collection: str, condition: dict) -> Cursor:
        return cls.client.get_database(db).get_collection(collection).find(condition)

    @classmethod
    def delete(cls, db: str, collection: str, condition: dict) -> DeleteResult:
        return cls.client.get_database(db).get_collection(collection).delete_one(condition)

    @classmethod
    def update(cls, db: str, collection: str, condition: dict, update: dict) -> UpdateResult:
        return cls.client.get_database(db).get_collection(collection).update_one(condition, update)


if __name__ == '__main__':
    # client = MongoTest.get_connection()
    # client = MongoClient('mongodb://root@localhost:27017/test?authSource=admin')
    # print(client.test.__class__)  # <class 'pymongo.database.Database'>
    # print(client.test.inventory.__class__)  # <class 'pymongo.collection.Collection'>

    # client.test.inventory.insert_one(
    #     {
    #         "item": "pymongo",
    #         "qty": 100,
    #         "tags": ["cotton"],
    #         "size": {"h": 28, "w": 35.5, "uom": "cm"}
    #     }
    # )

    # MongoTest.insert('test', 'inventory',
    #                  {
    #                      "item": "pymongo" + time.strftime('%Y%m%d%H%M%S', time.localtime()),
    #                      "qty": 100,
    #                      "tags": ["cotton"],
    #                      "size": {"h": 28, "w": 35.5, "uom": "cm"}
    #                  }
    #                  )
    for result in MongoTest.find('test', 'inventory', {}):
        pprint(result)
    MongoTest.delete('test', 'inventory', {'item': 'pymongo20201008204049'})
    MongoTest.update('test', 'inventory', {"item": "pymongo"},
                     {"$set": {"size.uom": "cm", "status": "P"},
                      "$currentDate": {"lastModified": True}})
