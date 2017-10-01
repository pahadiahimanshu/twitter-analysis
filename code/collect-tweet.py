import time
import tweepy
import json
import os
# from tweepy import Stream
# from tweepy import OAuthHandler
# from tweepy.streaming import StreamListener
from tweepy import User

# Make functions for easy use

# Change this hashtag for query
QUERY = 'FakeNews'


consumer_key = 'EtYBJlCZRg5KG3k6IlBzhBcWO'
consumer_secret = '1z3YZEQ3zZ2VM422jbwcsfdCtk7tWTTapH6Hw4BdB3nb5xXo6N'
access_token = '602494393-2bDuHWFELWezzUKDgvmSOEZrMwaON3ZWBZIc7apm'
access_token_secret = '3PhVqlQBTdxRCxrFS3RX0gW0leFRS0o1tI5ea7UCYzXGH'

# grabs system time
start_time = time.time()
# track list
keyword_list = ['twitter']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

print 'hey'
count = 0

panama_papers = tweepy.Cursor(api.search, q=QUERY, lang='en').items()
while count < 6804:
    try:
        tweet = panama_papers.next()
        count+=1
        # print tweet.created_at
        # print tweet.text
        # print "Time zone - ",tweet.user.time_zone
        geotag = ""
        # print "Location - ",tweet.user.location ==""
        # print "place - ",tweet.place == None    #returns none
        if tweet.place != None or tweet.coordinates != None:
            geotag = 'true'
        med = tweet.entities.get("media")
        entity = ""
        if med != None:
            # print 'media = ', med[0]["type"]    # returns photo
            if(med[0]["type"] == "photo"):
                entity +='1'
        # print 'urls = ', tweet.entities.get("urls") == []
        if(tweet.entities.get("urls") != []):
            entity += '2'
        # print 'user mentions = ', tweet.entities.get("user_mentions") == []
        if(tweet.entities.get("user_mentions") != []):
            entity +='3'
        # print 'symbols = ', tweet.entities.get("symbols") == []
        if( tweet.entities.get("symbols") != []):
            entity +='4'
        # print "entity - ",entity
        # print "1 = photo, 2 = urls, 3 = user mention, 4 = symbols"

        location = ""
        text = ""
        date = ""
        if(tweet.user.time_zone != None):
            location = tweet.user.time_zone
        if(tweet.text != None):
            text = tweet.text
            l = text.replace('|',' ')
            l = text.replace('\n',' ')
            l = text.replace('\r',' ')
            l = text.replace('~~',' ')

            l = text.replace('&amp;','and')
        if(tweet.created_at != None):
            date = str(tweet.created_at)
        raw_data = "created_at:"+date + "~~" + "tweet:" + l + "~~"+"country:"+location+"~~"+"entities:"+entity+"~~"+"geotag:"+geotag
        print str(count)+"TWEET ID + "+str(tweet.id)+"\n"+raw_data

        if not tweet.retweeted:
            saveFile = open(QUERY+'db-retweets.txt', 'a')
            raw_data.encode('utf-8')
            raw_data = raw_data.replace('\n',' ')
            saveFile.write(raw_data.encode('utf-8'))
            saveFile.write('\n')
            saveFile.close()
        else:
            count-=1
        # a = tweet.entities
        # print a['urls'] == []
        print '\n'
    except tweepy.TweepError, e:
        print 'failed - ', e
        time.sleep(60*15)
        continue
    except StopIteration:
        print "Stop iteration?"
        break
    print 'woaah'