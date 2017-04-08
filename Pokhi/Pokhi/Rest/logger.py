from dbConnect import mongo

class Logger:

    @staticmethod
    def Log(type,message):
        try:
            mongo.db.logs.insert({type:message})
        except Exception as e:
            print("Logger exception" , e)