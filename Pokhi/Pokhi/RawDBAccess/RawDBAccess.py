from pymongo import MongoClient

class RawDBAccess():

    @staticmethod
    def GetMongoDB():
        return RawDBAccess.MongoClient[RawDBAccess.DBName]

RawDBAccess.DBName = "python"
RawDBAccess.Credentials = 'mongodb://admin:DJ7FltP4ZWLY@localhost:27017/python'
RawDBAccess.MongoClient = MongoClient(RawDBAccess.Credentials)