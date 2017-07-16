import sys, time
from Pokhi.Pokhi.Rest.logger import Logger
from Pokhi.Pokhi.WebScrap.WikiScrap import WikiScrapper
from Pokhi.Pokhi.NLP.FeedChef import FeedChef
from Pokhi.Pokhi.RawDBAccess.RawDBAccess import RawDBAccess

class FeedCreateJob():
        def run(self):
            print("Running....")
            try:
                db = RawDBAccess.GetMongoDB()
                table = db.wikipediaFeed
                print("Starting ")
                Logger.Log("FeedJob" ,"Feed job starting")
                Logger.Log("FeedJob" ,"Feed job preparing feed")
                print("PrepareFeed....")
                WikiScrapper.PrepareFeed(table)
                Logger.Log("FeedJob" ,"Feed job processing feed")
                print("Process Feed....")
                chef = FeedChef()
                chef.ProcessRecords()
                Logger.Log("FeedJob" ,"Feed job processing feed done")
            except Exception as e:
                print(e)
                Logger.Log("Exception :FeedCreate job" ,e.message)
                

if __name__ == "__main__":
        daemon = FeedCreateJob()
        daemon.run()