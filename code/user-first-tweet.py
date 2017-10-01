import time
import tweepy

username = 'pahadiahimanshu'
consumer_key = 'EtYBJlCZRg5KG3k6IlBzhBcWO'
consumer_secret = '1z3YZEQ3zZ2VM422jbwcsfdCtk7tWTTapH6Hw4BdB3nb5xXo6N'
access_token = '602494393-2bDuHWFELWezzUKDgvmSOEZrMwaON3ZWBZIc7apm'
access_token_secret = '3PhVqlQBTdxRCxrFS3RX0gW0leFRS0o1tI5ea7UCYzXGH'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth)

user_tweets = api.user_timeline
user = api.get_user(username)
tweets = []
for tweet in tweepy.Cursor(api.user_timeline,id=username).items():
        tweets.append(tweet)

count = 1
for tweet in reversed(tweets):
    if count == 1:
        print tweet.created_at, tweet.text
    else:
        break
    count+=1

