import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import itertools
import collections
import tweepy as tw
import nltk
from nltk.corpus import stopwords
import re
import networkx
from textblob import TextBlob
import warnings


warnings.filterwarnings("ignore")
sns.set(font_scale=1.5)
sns.set_style("whitegrid")

consumer_key= 'DVvXmihjvAQ9Xz19Lc1ISVGa9'
consumer_secret= 'wMJwH7wVnppkmjXTYluq9gHkZEUIJbVPXV8T9XZ1pSP2JxIfEL'
access_token= '385212914-CZIj5V35XuyMOxebsIMHWqf9DbgCY1N8hSJG8ca4'
access_token_secret= 'nGPoaajrqurisX6aNeIoN5h1DzGPndsqnD1qAaODrLnN'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)


def remove_url(txt):
    """Replace URLs found in a text string with nothing 
    (i.e. it will remove the URL from the string).

    Parameters
    ----------
    txt : string
        A text string that you want to parse and remove urls.

    Returns
    -------
    The same txt string with url's removed.
    """

    return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", txt).split())

# Create a custom search term and define the number of tweets
search_term = "#IESS -filter:retweets"

tweets = tw.Cursor(api.search,
                   q=search_term,
                   lang="es",
                   since='2018-11-01').items(1000)

# Remove URLs
tweets_no_urls = [remove_url(tweet.text) for tweet in tweets]

# Create textblob objects of the tweets
sentiment_objects = [TextBlob(tweet) for tweet in tweets_no_urls]

sentiment_objects[0].polarity, sentiment_objects[0]

sentiment_values = [[tweet.sentiment.polarity, str(tweet)] for tweet in sentiment_objects]

sentiment_values[0]

sentiment_df = pd.DataFrame(sentiment_values, columns=["polaridad", "tweet"])

sentiment_df.head()

fig, ax = plt.subplots(figsize=(8, 6))

# Plot histogram of the polarity values
sentiment_df.hist(bins=[-1, -0.75, -0.5, -0.25, 0.25, 0.5, 0.75, 1],
             ax=ax,
             color="purple")

plt.title("Sentimientos de tweets sobre IESS")
plt.show()
