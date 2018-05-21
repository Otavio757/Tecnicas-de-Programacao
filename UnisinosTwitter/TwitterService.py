from twitter import Twitter, OAuth
from pprint import pprint
from inspect import getmembers
from TweetRepliedIndex import TweetRepliedIndex
from TweetCollection import TweetCollection

class TweetObject:
    def __init__(self, id, source, geo, text):
        self.id = id
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

def get_tweets(hashtag):
    t = get_twitter_instance()
    #a = t.statuses.home_timeline() # Get your "home" timeline
    a = t.search.tweets(q=hashtag, count=5)

    tweets = TweetCollection()

    for tweet in a['statuses']:
        idTweet = str(tweet).split("'id':")[1]
        idTweet = idTweet.split(",")[0]
        idTweet = int(idTweet)
        
        t = TweetObject(tweet["id"], tweet['source'], tweet['user']['location'], tweet['text'])
        tweets.append(t)
    return tweets #quem for printar pode usar item.__str__()

def make_tweet():
    t = get_twitter_instance()
    t.statuses.update(status="Using @sixohsix's sweet Python Twitter Tools..  #devopspower")

def reply_tweet(tweet_id, reply):
    t = get_twitter_instance()
    t.statuses.update(status=reply, in_reply_to_status_id=tweet_id, auto_populate_reply_metadata=True)

def send_direct_message(to, message): 
    t = get_twitter_instance()
    t.direct_messages.new(user=to, text=message)

def tweet_with_image(image_path):
    t = get_twitter_instance()
    # Send images along with your tweets:
    # - first just read images from the web or from files the regular way:
    with open(image_path, "rb") as imagefile:
        imagedata = imagefile.read()
    # - then upload medias one by one on Twitter's dedicated server and collect each one's id:
    t_upload = get_twitter_upload_instance()
    id_img1 = t_upload.media.upload(media=imagedata)["media_id_string"]
    #id_img2 = t_upload.media.upload(media=imagedata)["media_id_string"]
    # - finally send your tweet with the list of media ids:
    #t.statuses.update(status="PTT ★", media_ids=",".join([id_img1, id_img2]))
    t.statuses.update(status="PTT ★", media_ids=id_img1)

def analize(tweet):
    send_direct_message("trlthiago", "mensagem de teste")
    make_tweet()
    tweet_with_image("D:\\20180221_225728.jpg")

if __name__ == "__main__":

    #make_tweet()

    repliedTweetIndex = TweetRepliedIndex()
    
    tweets = get_tweets("#devopspower")

    print(tweets.GetInfo())

    for tweet in tweets:
        if not repliedTweetIndex.is_already_replied(tweet.id):
            repliedTweetIndex.set_as_replied(tweet.id)
