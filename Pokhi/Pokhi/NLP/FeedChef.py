from __future__ import absolute_import
from Pokhi.Pokhi.Rest.logger import Logger
from Pokhi.Pokhi.NLP.Helpers import Helpers
from Pokhi.Pokhi.WebScrap.WikiScrap import WikiScrapper
from Pokhi.Pokhi.RawDBAccess.RawDBAccess import RawDBAccess

class FeedChef(object):
    """Prepares the WikiPedia Feed After using NLP"""

    def __init__(self):
        self._lastId = 0
        self._wikipediaFeedCollection = "wikipediaFeed"
        self.ProcessedAllRecords = False

    def ProcessRecords(self):
        try:
            self.db = RawDBAccess.GetMongoDB()
            self.collection = self.db[self._wikipediaFeedCollection]

            while self.ProcessedAllRecords == False:
                for record in self.GetNext(self._lastId , 10) :
                    print("Got next 10 records")
                    try:
                        print("Beginning :  Keyword Extract")
                        keywords , keypoints = Helpers.ExtractKeywords(record["content"], 10)
                        print("Done : Keyword Extract")
                        record["keywords"] = keywords
                        record["keypoints"] = keypoints
                        record["isReady"] = True
                        self.collection.save(record)
                        print("Saved : Keyword Extract")
                    except Exception as e:
                        print(e)
                        Logger.Log("Feed Chef :Error processing record" , e.message)

        except Exception as e:
            print(e)
            Logger.Log("Feed Chef :Error accessing db" , e.message)

    def GetNext(self ,lastId, count=10):
        try:
            if(lastId == 0):
                records = list(self.collection.find({"isReady" : {"$exists" : False}} ).limit(count))
            else:
                records = list(self.collection.find({"$and" : [{"_id" :  {"$gt" :lastId} } , {"isReady" : {"$exists" : False}} ]}).limit(count))

            print(records)
            if len(records) > 1:
                self._lastId = records[-1]["_id"]
            else :
                self._lastId = -1
                self.ProcessedAllRecords = True
     
            return records
        except Exception as e:
            print(e)
            Logger.Log("FeedChef : Get Next" , e.message)
        return []


if __name__ == "__main__":
    chef = FeedChef()
    chef.ProcessRecords()


