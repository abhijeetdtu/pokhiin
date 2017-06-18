from pymongo import MongoClient
import os

class RawDBAccess():

    @staticmethod
    def GetMongoDB():
        return RawDBAccess.MongoClient[RawDBAccess.DBName]

RawDBAccess.DBName = "python"
RawDBAccess.Credentials = 'mongodb://admin:DJ7FltP4ZWLY@localhost:27017/python'

if('OPENSHIFT_MONGODB_DB_URL' in  os.environ):
    RawDBAccess.Credentials = os.environ['OPENSHIFT_MONGODB_DB_URL'] + 'python'

RawDBAccess.MongoClient = MongoClient(RawDBAccess.Credentials)