#enconding: utf-8

import sys, time
from datetime import datetime
from UnisinosClimaTempo.Chart import plot_weather
from UnisinosClimaTempo.DaysExtractor import TooMuchDaysAhead
from DependenceResolver import DependenceResolver

class UnisinosBot:
    def __init__(self, resolver):
        self.twitter = resolver.Resolve("twitter")
        self.weather = resolver.Resolve("weather")
        self.city = resolver.Resolve("city_extractor")
        self.days = resolver.Resolve("days_extractor")
        self.property = resolver.Resolve("property_extractor")
        self.repliedTweetIndex = resolver.Resolve("tweeter_index")

    def Show(self, tweet, cities, days):
        print(tweet.text)
        print(days.days_ahead)
        print(cities)

    def ExecuteRoutine(self):
        tweets = self.twitter.get_tweets("#tweet2timee")
        print(tweets.GetInfo() + str(datetime.now()))
        for tweet in tweets:
            
            if not self.repliedTweetIndex.is_already_replied(tweet.id):
                try:
                    print("=" * 60)
                    #cities = extractor.GetCities(tweet.text)
                    cities = self.city.SimpleExtratorEnsured(tweet.text)
                    days = self.days.get_raw_day(tweet.text)
                    
                    properties = self.property.get_cited_properties(tweet.text)

                    self.Show(tweet, cities, days)

                    if days.days_ahead == 0:
                        weather = self.weather.get_current_weather(cities[0])
                        #message = "A temperatura para %s hoje é %s" % (cities[0], weather.info[0].temperature)
                        message = weather.info[0].format_message(cities[0], properties)
                        self.twitter.reply_tweet(tweet.id, message)
                    else:
                        if days.is_exactly:
                            weathers = self.weather.get_weather_per_days(cities[0], exact_day=days.days_ahead)
                            print(weathers)
                            #message = "A temperatura para %s será %s" % (cities[0], weathers.info[0].temperature)
                            message = weathers.info[0].format_message(cities[0], properties)
                            self.twitter.reply_tweet(tweet.id, message)
                        else:
                            weathers = self.weather.get_weather_per_days(cities[0], days_ahead=days.days_ahead)
                            print(weathers)
                            if days.days_ahead >= 2:
                                plot_info = list(map(lambda x: [x.date, x.min_temperature], weathers.info))
                                chart_path = plot_weather(plot_info)
                                #message = "A temperatura para %s será %s" % (cities[0], weathers)
                                #message = " ".join([x.format_message(cities[0], properties) for x in weathers.info])
                                self.twitter.reply_tweet_with_image(tweet.id, "Acompanhe de forma visual a temperaura.", chart_path)
                            for info in weathers.info:
                                message = info.format_message(cities[0], properties)
                                self.twitter.reply_tweet(tweet.id, message)

                except TooMuchDaysAhead as e:
                    message = "Infelizmente não foi possível obter a previsão do tempo. Ela só está disponível até 5 dias a partir de hoje."
                    self.twitter.reply_tweet(tweet.id, message)

                except Exception as e:
                    print(e)
                    print(sys.exc_info()[0])

                self.repliedTweetIndex.set_as_replied(str(tweet.id))

if __name__ == "__main__":

    bot = UnisinosBot(DependenceResolver(False))

    while True:
        bot.ExecuteRoutine()
        time.sleep(30)
