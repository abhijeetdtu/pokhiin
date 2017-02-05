
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