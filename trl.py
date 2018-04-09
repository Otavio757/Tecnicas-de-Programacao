#!/usr/bin/env python

"""Password Pwned checker"""

__version__ = '0.1'
__author__ = 'Thiago Lopes'
__status__ = "Development"

from twitter import *
import urllib.request
from flask import Flask
from flask import request
from StringBuilder import StringBuilder
from Dataset import Dataset

app = Flask(__name__)

def load_twitter_tokens():
    f = open('twitter_settings.txt', 'r')
    settings = f.split(",")
    return settings

def start_twitter_monitoring():
    pass

def single_query_twitter(hashtag):
    settings = load_twitter_tokens()
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

@app.route('/')
def index():
    # sb = StringBuilder()
    sb = ""
    # sb.Append("Informe o termo de pesquisa: ")
    # sb.Append("<form method='get' action='/'>")
    # sb.Append("<input type='text' name='hashtag' />")
    # sb.Append("<input type='submit' value='Pesquisar' />")
    # sb.Append("</form>")
    sb+=("Informe o termo de pesquisa: ")
    sb+=("<form method='get' action='/pesquisar'>")
    sb+=("<input type='text' name='hashtag' />")
    sb+=("<input type='submit' value='Pesquisar' />")
    sb+=("</form>")
    sb+="<hr/>"
    sb+=("Leaked password checker: ")
    sb+=("<form method='get' action='/pwned'>")
    sb+=("<input type='text' name='hashtag' />")
    sb+=("<input type='submit' value='Pesquisar' />")
    sb+=("</form>")
    return sb

@app.route('/pesquisar')
def twitter_search():
    hashtag = request.args.get('hashtag')
    return single_query_twitter(hashtag)

# @app.route('/pwned')
# def twitter_search():
#     hashtag = request.args.get('hashtag')
#     obj = Dataset()
#     return obj.query_external_api(hashtag)

if __name__ == "__main__":
    app.run()



