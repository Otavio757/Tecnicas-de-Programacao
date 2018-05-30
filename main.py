import time
from datetime import datetime
from UnisinosTwitter.TwitterService import TwitterService
from UnisinosTwitter.TweetCollection import TweetCollection
from UnisinosTwitter.TweetRepliedIndex import TweetRepliedIndex
from UnisinosTwitter.CitiesExtractor import CitiesExtractor 
# from TweetRepliedIndex import TweetRepliedIndex
# from TweetCollection import TweetCollection
# from TwitterService import TwitterService

if __name__ == "__main__":
     # make_tweet("Como tá o tempo em Santo Antônio da Patrulha para amanhã #Tweet2Time")

    
    extractor = CitiesExtractor()
    cities = extractor.GetCities("Como está o tempo em gravataí")
    twitter = TwitterService()
    repliedTweetIndex = TweetRepliedIndex()

    while True:
    
        tweets = twitter.get_tweets("#devopspower") 

        print(tweets.GetInfo() + datetime.now().__str__())

        for tweet in tweets:
            if not repliedTweetIndex.is_already_replied(tweet.id):
                cities = extractor.GetCities(tweet.text)

                try:                    
                    twitter.reply_tweet(tweet.id, "Você está em " + cities[0] + "?")
                except:
                    pass
                    
                repliedTweetIndex.set_as_replied(str(tweet.id))
        
        time.sleep(2)
