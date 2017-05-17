from dbConnect import mongo
import datetime

class Logger:

    @staticmethod
    def Log(type,message):
        try:
            mongo.db.logs.insert({"type":type, "message":message , "createdDateTime" : datetime.datetime.now()})
        except Exception as e:
            print("Logger exception" , e.message)