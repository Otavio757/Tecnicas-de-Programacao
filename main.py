import sys
import time
from pprint import pprint
from datetime import datetime
from UnisinosTwitter.TwitterService import TwitterService, TwitterServiceFake
from UnisinosTwitter.TweetCollection import TweetCollection
from UnisinosTwitter.TweetRepliedIndex import TweetRepliedIndex
from UnisinosTwitter.CitiesExtractor import CitiesExtractor 
from UnisinosClimaTempo.DaysExtractor import DaysExtractor
from UnisinosClimaTempo.ClimaTempoService import ClimaTempoService
from UnisinosClimaTempo.Chart import plot_weather


if __name__ == "__main__":

    extractor = CitiesExtractor()
    cities = extractor.GetCities("Como está o tempo em gravataí")
    #twitter = TwitterService()
    twitter = TwitterServiceFake()
    repliedTweetIndex = TweetRepliedIndex()
    daysExtractor = DaysExtractor()
    climaTempo = ClimaTempoService(isDebug=True)

    while True:
    
        tweets = twitter.get_tweets("#devopspower") 

        #print(tweets.GetInfo() + datetime.now().__str__())

        for tweet in tweets:
            if not repliedTweetIndex.is_already_replied(tweet.id):
                #cities = extractor.GetCities(tweet.text)
                cities = extractor.SimpleExtratorEnsured(tweet.text)
                try: 
                    days = daysExtractor.get_raw_day(tweet.text)
                    print("=" * 60)
                    print(tweet.text)
                    print(days.days_ahead)
                    print(cities)
                    
                    if days.days_ahead == 0:
                        weather = climaTempo.get_current_weather(cities[0])
                        message = "A temperatura para %s hoje é %s" % (cities[0], weather.info[0].temperature)
                        print(message)
                        #twitter.reply_tweet(tweet.id, message)
                    else:
                        weathers = climaTempo.get_weather_per_days(cities[0])
                        if days.is_exactly:
                                print(weathers.info[days.days_ahead].Format())
                        else:
                            plot_info = list(map(lambda x: [x.date, x.min_temperature], weathers.info))
                            chart_path = plot_weather(plot_info)
                            for weather in weathers.info[0:days.days_ahead]:
                                print(weather.Format())
                            #twitter.reply_tweet_with_image(tweet.id, message, chart_path)
                except:
                    print(sys.exc_info()[0])
                    
                repliedTweetIndex.set_as_replied(str(tweet.id))
        
        time.sleep(2)
