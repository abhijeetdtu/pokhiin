import sys, time
from Pokhi.Pokhi.Rest.logger import Logger
from Pokhi.Pokhi.OPS.Daemon import Daemon
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
                while True:
                    print("PrepareFeed....")
                    WikiScrapper.PrepareFeed(table)
                    print("Process Feed....")
                    chef = FeedChef()
                    chef.ProcessRecords()
                    print("Sleep....10 mins starting now.." +  str(time.time))
                    time.sleep(10*60)
            except Exception as e:
                print(e)
                Logger.Log("Exception :FeedCreate job" ,e.message)
                

if __name__ == "__main__":
        daemon = FeedCreateJob()
        daemon.run()