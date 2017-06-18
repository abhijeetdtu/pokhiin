import sys, time
from Pokhi.Pokhi.Rest.logger import Logger
from Pokhi.Pokhi.OPS.Daemon import Daemon
from Pokhi.Pokhi.WebScrap.WikiScrap import WikiScrapper
from Pokhi.Pokhi.NLP.FeedChef import FeedChef
from Pokhi.Pokhi.RawDBAccess.RawDBAccess import RawDBAccess

class FeedCreateJob(Daemon):
        def run(self):
            try:
                db = RawDBAccess.GetMongoDB()
                table = db.wikipediaFeed
                print("Starting ")
                while True:
                
                    WikiScrapper.PrepareFeed(table)
                    chef = FeedChef()
                    chef.ProcessRecords()
                    time.sleep(10*60)
            except Exception as e:
                print(e)
                Logger.Log("Exception :FeedCreate job" ,e.message)
                

if __name__ == "__main__":
        daemon = FeedCreateJob('/tmp/FeedCreateJob.pid')
        if len(sys.argv) == 2:
                if 'start' == sys.argv[1]:
                        daemon.start()
                elif 'stop' == sys.argv[1]:
                        daemon.stop()
                elif 'restart' == sys.argv[1]:
                        daemon.restart()
                else:
                        print "Unknown command"
                        sys.exit(2)
                sys.exit(0)
        else:
                print "usage: %s start|stop|restart" % sys.argv[0]
                sys.exit(2)