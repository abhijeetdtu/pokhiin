import math
from random import randint
class Helpers:
    
    @staticmethod
    def  GetProperties(obj , propArray = None):
        retobj = {}
    
        retobj["_id"] = str(obj["_id"])
        print(retobj)
        if(propArray == None):
            for x in obj:
                if(x != '_id'):
                    retobj[x] = obj[x]
        else:
            for x in propArray:
                if(x != '_id'):
                    retobj[x] = obj[x]
        return retobj
    
    @staticmethod
    def CollectionToArray(collection):
        return [Helpers.GetProperties(x) for x in collection]

    @staticmethod
    def GetRandomString(length):
        return "".join([chr(randint(65,91)) for x in range(length)])