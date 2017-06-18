from __future__ import absolute_import
from Pokhi.Pokhi.Rest.logger import Logger
from Pokhi.Pokhi.Rest.config import Config

from Pokhi.Pokhi.NLP.Helpers import Helpers
from Pokhi.Pokhi.RawDBAccess.RawDBAccess import RawDBAccess


import numpy as np
import cv2
import os
import urllib
from collections import defaultdict

class FeedChef(object):
    """Prepares the WikiPedia Feed After using NLP"""

    def __init__(self):
        self._lastId = 0
        self._wikipediaFeedCollection = "wikipediaFeed"
        self.ProcessedAllRecords = False

    def ProcessRecords(self , refresh = False ,func=None):
        try:
            self.db = RawDBAccess.GetMongoDB()
            self.collection = self.db[self._wikipediaFeedCollection]
            if refresh == True:
                self.collection.update({} , {"$unset" :{"isReady" : ""}})

            while self.ProcessedAllRecords == False:
                for record in self.GetNext(self._lastId , 10) :
                    print("Got next 10 records")
                    if func != None:
                        try:
                            func(record)
                        except Exception as e:
                            print(e)
                            Logger.Log("Feed chef custom function error" , e.message)
                            continue
                    else:
                        try:
                            print("Beginning :  Keyword Extract")
                            keywords , keypoints = Helpers.ExtractKeywords(record["content"], 10)
                            print("Done : Keyword Extract")
                            record["keywords"] = keywords
                            record["keypoints"] = keypoints
                            
                            print("Saved : Keyword Extract")
                        except Exception as e:
                            print(e)
                            Logger.Log("Feed Chef :Error processing record" , e.message)
                    record["isReady"] = True
                    self.collection.save(record)

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

    def ProcessRankImages(self,record):
        record["images"] = self.RankImages(record["images"])

    def RankImages(self , images):
        ranks = defaultdict(int)
        try:
            for image in images:
                if image.find("svg") < 0:
                    try:
                        face_cascade = cv2.CascadeClassifier(os.path.abspath(os.path.join(Config.ENV["OPEN_CV_HOME"] , 'haarcascades\haarcascade_frontalface_default.xml')))
                        img = self.GetImageFromURL(image)
                        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
                        ranks[image] = len(list(faces))
                        print("face count : " ,ranks[image] )
                    except Exception as e:
                        print("Exception: " , e)
                        Logger.Log("Feed chef:Rank Images:image processing error" , e.message)
                        ranks[image] = -1
                        continue

            inverserMat = [x[0] for x in sorted(ranks.items() , key= lambda x: x[1], reverse= True)]
            return inverserMat
        except Exception as e:
            print("Exception: " , e)
            Logger.Log("FeedChef Error:Rank Images:" , e.message)
            return images
    
    def GetImageFromURL(self , url):
        try:
            url_response = urllib.urlopen(url)
            img_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
            img = cv2.imdecode(img_array, -1)
            print("got image" , img != None)
            return img
        except Exception as e:
            print("Exception : " , e)
            Logger.Log("FeedChef:GetImageFromURL" , e.message)
            return None

if __name__ == "__main__":
    chef = FeedChef()
    #chef.ProcessRecords()
    chef.ProcessRecords(refresh = True ,func = chef.ProcessRankImages)
    #print(chef.RankImages(["http://bbcpersian7.com/images/book-image-12.jpg", "https://static.pexels.com/photos/56875/tree-dawn-nature-bucovina-56875.jpeg","https://upload.wikimedia.org/wikipedia/commons/6/61/Zayn_Malik_April_2014.png" ]))


