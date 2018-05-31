from twitter import Twitter, OAuth
from pprint import pprint
from inspect import getmembers
from UnisinosTwitter.TweetRepliedIndex import TweetRepliedIndex
from UnisinosTwitter.TweetCollection import TweetCollection
from UnisinosTwitter.TweetObject import TweetObject

class TwitterService:

    def load_twitter_tokens(self):
        with open('Settings/twitter_settings.txt', 'r') as content_file:
            content = content_file.read()
            settings = content.split(",")
            return settings

    def start_twitter_monitoring(self):
        pass

    def get_twitter_instance(self):
        settings = self.load_twitter_tokens()
        return Twitter(auth=OAuth(settings[0], settings[1], settings[2], settings[3]))

    def get_twitter_upload_instance(self):
        settings = self.load_twitter_tokens()
        return Twitter(domain="upload.twitter.com", auth=OAuth(settings[0], settings[1], settings[2], settings[3]))

    def get_tweets(self, hashtag):
        t = self.get_twitter_instance()
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

    def make_tweet(self, text):
        t = self.get_twitter_instance()
        t.statuses.update(status=text)

    def reply_tweet(self, tweet_id, reply):
        t = self.get_twitter_instance()
        t.statuses.update(status=reply, in_reply_to_status_id=tweet_id, auto_populate_reply_metadata=True)

    def send_direct_message(self, to, message): 
        t = self.get_twitter_instance()
        t.direct_messages.new(user=to, text=message)

    def tweet_with_image(self, image_path):
        t = self.get_twitter_instance()
        # Send images along with your tweets:
        # - first just read images from the web or from files the regular way:
        with open(image_path, "rb") as imagefile:
            imagedata = imagefile.read()
        # - then upload medias one by one on Twitter's dedicated server and collect each one's id:
        t_upload = self.get_twitter_upload_instance()
        id_img1 = t_upload.media.upload(media=imagedata)["media_id_string"]
        #id_img2 = t_upload.media.upload(media=imagedata)["media_id_string"]
        # - finally send your tweet with the list of media ids:
        #t.statuses.update(status="PTT ★", media_ids=",".join([id_img1, id_img2]))
        t.statuses.update(status="PTT ★", media_ids=id_img1)

    def analize(self, tweet):
        self.send_direct_message("trlthiago", "mensagem de teste")
        self.make_tweet("Replying ")
        self.tweet_with_image("D:\\20180221_225728.jpg")

if __name__ == "__main__":

    #make_tweet("Como tá o tempo em Santo Antônio da Patrulha para amanhã #Tweet2Time")

    repliedTweetIndex = TweetRepliedIndex()
    twitter = TwitterService()
    tweets = twitter.get_tweets("#devopspower")

    print(tweets.GetInfo())

    for tweet in tweets:
        if not repliedTweetIndex.is_already_replied(tweet.id):
            repliedTweetIndex.set_as_replied(tweet.id)
            #reply_tweet()
