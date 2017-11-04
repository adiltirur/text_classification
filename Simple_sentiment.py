import tweepy
from textblob import TextBlob

consumer_key= 'Your consumer_key Here'
consumer_secret= 'Your consumer_secret Here'

access_token='Your Acess Token Here'
access_token_secret='Your token_decret Here'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Your Message here')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
