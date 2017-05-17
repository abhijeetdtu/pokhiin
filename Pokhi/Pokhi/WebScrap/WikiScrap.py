
import time
import datetime
import wikipedia
from pymongo import MongoClient

from Pokhi.Pokhi.Rest.logger import Logger
from Pokhi.Pokhi.Rest.dbAccess import WikipediaFeed as WikiFeed
from Pokhi.Pokhi.WebScrap.TwitterAPI import TwitterAPI

class WikiScrapper:


    @staticmethod
    def GetPage(topic):
        try:
            page = wikipedia.page(topic)
            return {"topic" : topic , "title":page.title.replace("\"" , "\\\"")  , "images": page.images ,"content" : page.content.replace("\"" , "\\\"") , "summary": page.summary.replace("\"" , "\\\"") ,"createddatetime" : str(datetime.datetime.now())}
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
        return feed

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
        except Exception as e:
            print(e)
            Logger.Log("Error WikiScrapper.PrepareFeed" , e.message)

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

