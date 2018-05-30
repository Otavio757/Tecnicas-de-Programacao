__version__ = '0.1'
__author__ = 'Thiago Lopes'
__status__ = "Development"

class TweetCollection:
    def __init__(self):
        self.tweets = []

    def __str__(self):
        return self.GetInfo()

    def __iter__(self):
        for x in self.tweets:
            yield x

    def GetInfo(self):
        length = len(self.tweets)
        x = str(length) + " tweets retuned."
        for tweet in self.tweets:
            x += tweet.__str__()
        return x

    def append(self, tweet):
        self.tweets.append(tweet)

    