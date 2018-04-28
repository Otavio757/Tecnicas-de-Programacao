from twitter import *
from pprint import pprint
from inspect import getmembers

class TweetCollection:
    def __init__(self):
        self.tweets = []
    
    def append(self, tweet):
        self.tweets.append(tweet)

    def __str__(self): 
        for tweet in self.tweets:
            return tweet.__str__()
    
    def PrintInfo():
        print(str(len(a['statuses'])) + " tweets retuned.")

class Tweet:
    def __init__(self, source, geo, text):
        self.geo = geo
        self.text = text
        self.source = source

    def __str__(self): 
        return f"{self.source} - {self.geo} - {self.text}."

def load_twitter_tokens():
    with open('twitter_settings.txt', 'r') as content_file:
        content = content_file.read()
        settings = content.split(",")
        return settings

def start_twitter_monitoring():
    pass

def single_query_twitter(hashtag):
    settings = load_twitter_tokens()
    t = Twitter(auth=OAuth(settings[0], settings[1], settings[2], settings[3]))

    #a = t.statuses.home_timeline() # Get your "home" timeline
    a = t.search.tweets(q=hashtag, count=5)

    tc = TweetCollection()

    for tweet in a['statuses']:
        t = Tweet(tweet['source'], tweet['user']['location'], tweet['text'])
        tc.append(t)
        tweets.append(t)
    return tc #quem for printar pode usar item.__str__()


if __name__ == "__main__":
    tc = single_query_twitter("#devopspower")
    print(tc)