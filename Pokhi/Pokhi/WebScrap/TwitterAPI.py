from __future__ import absolute_import
import twitter
import re


class TwitterAPI:
    
    @staticmethod
    def GetTrends():
        trends = []
        twitterTrends = TwitterAPI.API.GetTrendsWoeid(TwitterAPI.WOEIDIndia)
        twitterTrends += TwitterAPI.API.GetTrendsCurrent()
        for trend in twitterTrends:
            trendDic = trend.AsDict()
            print(trendDic)
            try:
                hashTagToWord = " ".join(re.findall(TwitterAPI.HashTagToWordRegex, trendDic["name"]))
                trends.append(hashTagToWord)
                print(hashTagToWord)
            except Exception as e:
                continue
            pass
        print(trends)
        return trends

TwitterAPI.HashTagToWordRegex = "[A-Z][a-z\d]+|[A-Z]+|A"
TwitterAPI.WOEIDIndia = 23424848
TwitterAPI.CONSUMER_KEY = "Mgw2AhNY35Mu7dReefdQHlsRs"
TwitterAPI.CONSUMER_SECRET = "rNc5n9pI9bIM1N6aU50bGVu9vKqFEbimsTB5Q7DoSv2KfQRKH5"
TwitterAPI.ACCESS_TOKEN_KEY = "2432380130-0UM4lm5xnj4583ixO9T46cHQSdMruGJQmZkid4K"
TwitterAPI.ACCESS_TOKEN_SECRET = "rujHp9z3AhQfEn25uPpyX20dNR2oIdbox1iJDRVTLyZ6f"
TwitterAPI.API =  twitter.Api(consumer_key=TwitterAPI.CONSUMER_KEY,
                      consumer_secret=TwitterAPI.CONSUMER_SECRET,
                      access_token_key=TwitterAPI.ACCESS_TOKEN_KEY,
                      access_token_secret=TwitterAPI.ACCESS_TOKEN_SECRET)


if __name__ == "__main__":
    TwitterAPI.GetTrends()




    

