# coding=utf-8

from pymongo import MongoClient

client = MongoClient('127.0.0.1', 27018)
db = client.novel
