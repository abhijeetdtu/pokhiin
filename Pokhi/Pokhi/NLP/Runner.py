from __future__ import absolute_import
from Pokhi.Pokhi.NLP.Helpers import Helpers
from Pokhi.Pokhi.WebScrap.WikiScrap import WikiScrapper
from Pokhi.Pokhi.RawDBAccess.RawDBAccess import RawDBAccess
from Pokhi.Pokhi.NLP.Recommender import Recommender

import re 
from collections import defaultdict


def ScrubImages():
    reg = "logo|edit\-clear|icon|padlock\-silver|blue_pencil|ambox_important|portal\-puzzle|symbol|lock\-green|p_vip" 
    db = RawDBAccess.GetMongoDB()
    collection = db["wikipediaFeed"]
    for doc in collection.find():
        array= doc["images"]
        doc["images"] = [x for x in array if not re.search(reg,x , re.IGNORECASE)]
        collection.save(doc)

def GetFrequencyCountImages():

    images= defaultdict(int)
    db = RawDBAccess.GetMongoDB()
    collection = db["wikipediaFeed"]
    for doc in collection.find():

        for image in doc["images"]:
            images[image] += 1
        
        #doc["summary"]  = re.sub(r"[ ]+" , " ", re.sub(r"[\r\n=]" ," ", doc["summary"])).strip(" ")
        #doc["content"]  = re.sub(r"[ ]+" , " ", re.sub(r"[\r\n=]" ," ", doc["content"])).strip(" ")
        #doc["summary"]  = re.sub(r"[ ]+" , " ", doc["summary"]) 
        #doc["content"]  = re.sub(r"[ ]+" , " ", doc["content"])   
        #collection.save(doc)
    out = ""

    sortedByCount = sorted(images.items() , key = lambda x : x[1])

    out = ["\n" +key + ":" + str(val) for key,val in sortedByCount]

    fi = open("out.txt", "w")
    fi.write("\n".join(out))
    fi.close()

if __name__ == '__main__':
   rec = Recommender()
   rec.TrainModel(newsGroup=True)
   #rec = Recommender(load=True)
   #rec.TestModel()
