from clima_tempo import Weather, citiesDictionary, loadCitiesIDs
from datetime import date
from UnisinosTwitter.TweetRepliedIndex import TweetRepliedIndex
from UnisinosTwitter.TwitterService import get_tweets, reply_tweet

#Dicionário com as palavras-chave que serão verificadas no tweet do usuário
keyWords = {}
numbers = {}


def start():
    loadCitiesIDs()
    generateKeyWordsAndNumbers()
    tweets = getTweets()
    
    for tweet in tweets: #range(0, len(tweets.tweets)):
        #tweet = tweets.tweets[i]
        text = getTweetText(tweet)
        
        city = checkCity(text)
        w = Weather(city)
        
        day = checkDay(text)
        
        try:
            day = int(day)
            forecast = w.getForecastOneDay(day)
            allProperties = w.getAllPropertiesForecastOneDay(forecast)

            message = w.getPropertyForecastByIndexOneDay(8, forecast)
            reply_tweet(tweet.id, message)

            print(allProperties)
        
        except ValueError:
            todayNumber = date.today().weekday() + 1
            
            if (todayNumber > 6):
                todayNumber = 0
                
            split = day.split(":")
            lastDay = int(split[1])
            forecast = w.getForecastIntervalOfDays(1, lastDay)
            
            allProperties = "----- " + weekDays[todayNumber].upper() + " -----\n\n" + w.getAllPropertiesForecastOneDay(forecast[0])

            message = weekDays[todayNumber] + ": " + w.getPropertyForecastByIndexOneDay(8, forecast[0])

            cont = todayNumber + 1
            
            for j in range(1, len(forecast)):
                if(cont > 6):
                    cont = 0
                    
                allProperties += "\n\n----- " + weekDays[cont].upper() + " -----\n\n" + w.getAllPropertiesForecastOneDay(forecast[j])
                message += "\n" + weekDays[cont] + ": " + w.getPropertyForecastByIndexOneDay(8, forecast[j])
                cont += 1
            
            reply_tweet(tweet.id, tweet)
            print(allProperties)
        


def getTweets():
    tweets = get_tweets("#Tweet2Time")
    
    if (len(tweets.tweets) == 0):
        tweets = get_tweets("#TweetToTime")

    return tweets

def getTweetText(tweet):
    tweetString = str(tweet)
    text = tweetString.split(" - ")[2]
    
    return text

#Este método retorna um número ou intervalo de dias para calcular a previsão do tempo

                    

