from twitter import *

def load_twitter_tokens():
    with open('twitter_settings.txt', 'r') as content_file:
        content = content_file.read()
        settings = content.split(",")
        return settings

def start_twitter_monitoring():
    pass

def single_query_twitter(hashtag):
    settings = load_twitter_tokens()
    print(settings)
    t = Twitter(auth=OAuth(settings[0], settings[1], settings[2], settings[3]))

    # Get your "home" timeline
    #a = t.statuses.home_timeline()

    a = t.search.tweets(q=hashtag, count=5)

    # sb = StringBuilder()
    sb=""
    print("COUNT = " + str(len(a['statuses'])))

    for tweet in a['statuses']:
        print (tweet['source'])
        print (tweet['text'])
        print ("\r\n")
        sb+=(tweet['source'])
        sb+=(tweet['text'])
        sb+=("<br/>")
    return sb