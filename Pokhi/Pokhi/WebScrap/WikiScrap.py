
import time
import datetime
import wikipedia
import re

from pymongo import MongoClient

from Pokhi.Pokhi.Rest.logger import Logger
from Pokhi.Pokhi.Rest.dbAccess import WikipediaFeed as WikiFeed
from Pokhi.Pokhi.WebScrap.TwitterAPI import TwitterAPI

if __name__ == '__main__':
    from Pokhi.Pokhi.NLP.FeedChef import FeedChef

class WikiScrapper:
    
    @staticmethod
    def GetPage(topic):
        try:
            page = wikipedia.page(topic)
            return {"topic" : topic , "title":page.title.replace("\"" , "\\\"")  , "images": WikiScrapper.ScrubImageArray(page.images) ,"content" : page.content.replace("\"" , "\\\"") , "summary": page.summary.replace("\"" , "\\\"") ,"createddatetime" : str(datetime.datetime.now())}
        except Exception as e:
            print(e)
            Logger.Log("Error" , e.message)
            return None


    @staticmethod
    def GetFeed(lastId , count=2):
        try:
            feed = WikiFeed.GetPages(lastId)
        except Exception as e:
            print(e)
            Logger.Log("Error WikiScrapper.GetFeed" , e.message)
            return [{"topic" : topic , "title":"LoremIpsem" , "images": [""] ,"content" : "No content" , "summary": "No page retrieved" }]
        return {"feed" : feed , "lastId" : feed[-1]["createddatetime"]}

    @staticmethod
    def PrepareFeed(table):
        try:
            topics = WikiScrapper.GetTopics()
            for topic in topics:
                try:
                    print("Getting page for" , topic)
                    page = WikiScrapper.GetPage(topic)
                    print("Saving page to Db" , topic)
                    if page != None:
                        AddPageToDB(table,page)
                except Exception as e:
                    print(e)
                    Logger.Log("Error WikiScrapper.PrepareFeed Inner Loop" , e.message)
                    continue
            chef = FeedChef()
            chef.ProcessRecords()
        except Exception as e:
            print(e)
            Logger.Log("Error WikiScrapper.PrepareFeed" , e.message)
    
    @staticmethod
    def ScrubImageArray(array):
        reg = "logo|edit\-clear|icon|padlock\-silver|blue_pencil|ambox_important|portal\-puzzle|symbol|lock\-green|p_vip"
        array = [x for x in array if not re.search(reg,x , re.IGNORECASE)]
        return array
      
    @staticmethod
    def GetTopics():
        return  TwitterAPI.GetTrends()


def AddPageToDB(table ,page):
    try:
        table.insert_one(page)
    except Exception as e:
        print(e)
        Logger.Log("Error WikiScrapper.PrepareFeed Inner Loop" , e.message)

if __name__ == '__main__':

    client = MongoClient('mongodb://admin:DJ7FltP4ZWLY@localhost:27017/python')
    db = client.python
    table = db.wikipediaFeed
    #table.insert_one({"name" : "hello"})
    WikiScrapper.PrepareFeed(table)

