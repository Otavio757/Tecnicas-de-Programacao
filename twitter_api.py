from twitter import *
from pprint import pprint
from inspect import getmembers

class TweetCollection:
    def __init__(self):
        self.tweets = []
    
    def append(self, tweet):
        self.tweets.append(tweet)

    def __str__(self):
        return self.GetInfo()

    def GetInfo(self):
        length = len(self.tweets)
        x = str(length) + " tweets retuned."
        for tweet in self.tweets:
            x += tweet
        return x

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

def get_twitter_instance():
    settings = load_twitter_tokens()
    return Twitter(auth=OAuth(settings[0], settings[1], settings[2], settings[3]))

def get_twitter_upload_instance():
    settings = load_twitter_tokens()
    return Twitter(domain="upload.twitter.com", auth=OAuth(settings[0], settings[1], settings[2], settings[3]))

def single_query_twitter(hashtag):
    t = get_twitter_instance()
    #a = t.statuses.home_timeline() # Get your "home" timeline
    a = t.search.tweets(q=hashtag, count=5)

    tweets = TweetCollection()

    for tweet in a['statuses']:
        t = Tweet(tweet['source'], tweet['user']['location'], tweet['text'])
        tweets.append(t)
    return tweets #quem for printar pode usar item.__str__()

def make_tweet():
    t = get_twitter_instance()
    t.statuses.update(status="Using @sixohsix's sweet Python Twitter Tools..", in_reply_to_status_id="901156381490917376", auto_populate_reply_metadata=True)

def  send_direct_message(to, message): 
    t = get_twitter_instance()
    t.direct_messages.new(user=to, text=message)

def tweet_with_image():
    t = get_twitter_instance()
    # Send images along with your tweets:
    # - first just read images from the web or from files the regular way:
    with open("example.png", "rb") as imagefile:
        imagedata = imagefile.read()
    # - then upload medias one by one on Twitter's dedicated server and collect each one's id:
    t_upload = get_twitter_upload_instance()
    id_img1 = t_upload.media.upload(media=imagedata)["media_id_string"]
    id_img2 = t_upload.media.upload(media=imagedata)["media_id_string"]
    # - finally send your tweet with the list of media ids:
    t.statuses.update(status="PTT ★", media_ids=",".join([id_img1, id_img2]))

if __name__ == "__main__":
    #tc = single_query_twitter("#devopspower")
    #print(tc)
    #send_direct_message("trlthiago", "mensagem de teste")
    make_tweet()