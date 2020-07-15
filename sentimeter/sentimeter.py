__author__ = 'markdown'
from secrets import Oauth_Secrets
import tweepy 
from textblob import TextBlob

def primary(input_hashtag):
    secrets = Oauth_Secrets()
    auth = tweepy.OAuthHandler(secrets.consumer_key, secrets.consumer_secret)
    auth.set_access_token(secrets.access_token, secrets.access_token_secret)

    api = tweepy.API(auth)

    N = 1000
    Tweets = tweepy.Cursor(api.search, q=input_hashtag, rpp=50).items(N)

    sara = 0
    non_sara = 0
    sara_count = 0 
    neutral_count = 0 
    non_sara_count = 0 

    for tweet in Tweets: 
        print(tweet.text)
        # print(tweet.user.screen_name)

        blob = TextBlob(tweet.text)
        if blob.sentiment.polarity <= -0.1: 
            sara = blob.sentiment.polarity 
            sara_count += 1 
        elif blob.sentiment.polarity >= 0.1:
            non_sara_count += 1
        else: 
            blob.sentiment.polarity 
            neutral_count += 1 

        
        print("Total tweets",N)
        print("Non_sara ",float(non_sara_count/N)*100,"%")
        print("Sara ",float(sara_count/N)*100,"%")
        print("Neutral ",float(neutral_count/N)*100,"%")

    return [['Sentiment', 'no. of tweets'], ['Non sara',non_sara_count]
            ,['Neutral', neutral_count],['Sara', sara_count]]
        
