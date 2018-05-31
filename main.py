import sys
import time
from pprint import pprint
from datetime import datetime
from UnisinosTwitter.TwitterService import TwitterService
from UnisinosTwitter.TweetCollection import TweetCollection
from UnisinosTwitter.TweetRepliedIndex import TweetRepliedIndex
from UnisinosTwitter.CitiesExtractor import CitiesExtractor 
from UnisinosClimaTempo.DaysExtractor import DaysExtractor
from UnisinosClimaTempo.ClimaTempoService import ClimaTempoService
# from TweetRepliedIndex import TweetRepliedIndex
# from TweetCollection import TweetCollection
# from TwitterService import TwitterService

if __name__ == "__main__":
     # make_tweet("Como tá o tempo em Santo Antônio da Patrulha para amanhã #Tweet2Time")

    extractor = CitiesExtractor()
    cities = extractor.GetCities("Como está o tempo em gravataí")
    twitter = TwitterService()
    repliedTweetIndex = TweetRepliedIndex()
    daysExtractor = DaysExtractor()
    climaTempo = ClimaTempoService(isDebug=False)

    # print(daysExtractor.get_raw_day("qual a previsao do tempo para gravatai nos proximos 10 dias?"))
    # print(daysExtractor.get_raw_day("qual a previsao do tempo para gravatai nos proximos dez dias?"))
    # print(daysExtractor.get_raw_day("qual a previsao do tempo pra são leopoldo pra hoje?"))
    # print(daysExtractor.get_raw_day("qual a previsao do tempo para canoas pra sexta feira?"))
    # print(daysExtractor.get_raw_day("qual a previsao do tempo para glorinha amanhã?"))

    while True:
    
        tweets = twitter.get_tweets("#devopspower") 

        #print(tweets.GetInfo() + datetime.now().__str__())

        for tweet in tweets:
            if not not repliedTweetIndex.is_already_replied(tweet.id):
                cities = extractor.GetCities(tweet.text)
                try: 
                    days = daysExtractor.get_raw_day(tweet.text)
                    days = 6
                    print(days)
                    print(cities)

                    if days == 0:
                        weather = climaTempo.get_current_weather(cities[0])
                        tweet = "A temperatura para %s hoje é %s" % cities[0], weather.info[0].temperature
                        #twitter.reply_tweet(tweet.id, tweet)
                    else:
                        weathers = climaTempo.get_weather_per_days(cities[0])
                        for weather in weathers.info[0:days]:
                            print(weather.Format())

                except:
                    print(sys.exc_info()[0])
                    
                repliedTweetIndex.set_as_replied(str(tweet.id))
        
        time.sleep(2)
