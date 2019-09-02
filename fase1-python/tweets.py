import pandas as pd
import tweepy as tw
from textblob import TextBlob
import collections

import nltk
from nltk.corpus import stopwords
import re
import networkx
import warnings




#Credenciales de acceso

consumer_key= 'FjkPX4EdbaKQL8CQnX1maCHX0'
consumer_secret= '8XmViZ9ZRtp96UaueWktTwXUy2yIZ8lmG9IYFs0P264nKVWzAV'
access_token= '385212914-XGthY2ZCCTmPmqlmRkmvATMi7fQUQ6LUzuWO5uNV'
access_token_secret= 'doSh08Z4Vph6ZtKwhY4xfxLT0JWc40zoKIwU902DTQVLT'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

print(api.me().name)

# # Crear una busqueda con el termino IESS
# search_term = "#IESS"

def remove(txt):
       return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", txt).split())
def buscayguardaTweets(busqueda):
    tweets = tw.Cursor(api.search, q=busqueda,lang="es",since='2018-11-01').items(500)
    tweetsurl =[ remove(tweet.text) for tweet in tweets]
    sentiment_objects = [TextBlob(tweet) for tweet in tweetsurl]
    sentiment_objects[0].polarity, sentiment_objects[0]
    sentiment_values = [[tweet.sentiment.polarity, str(tweet)] for tweet in sentiment_objects]
    sentiment_values[0]
    sentiment_df = pd.DataFrame(sentiment_values, columns=["polaridad", "tweet"])
    sentiment_df.to_csv('tweets'+busqueda+'.csv', encoding='utf-8')
    print('tweets guardados de:'+busqueda)

buscayguardaTweets('#IESS')
buscayguardaTweets('#SRI')
buscayguardaTweets('#CPCCS')