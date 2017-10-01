import os
import string
import operator
import numpy as np
from datetime import datetime
import time
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import plotly
plotly.tools.set_credentials_file(username='pahadiahimanshu', api_key='uiwghXmjaWrzcLd2LiQC')

import plotly.plotly as py
import plotly.graph_objs as go

# nltk.download("stopwords")

# Make functions for easy use & use some database instead of text file for storing tweets

# Change the database file name here
FILE = 'fakenewsdb-retweets.txt'
OUTPUT = 'fakenews'

stop_words = set(stopwords.words('english'))
# print stop_words
stop_words.add('do')
stop_words.add('')
stop_words.add('the')
stop_words.add('\xe2\x80\xa6')

# geo tag tweet counter
geotag_counter = 0

# entities variables
photos_count = 0
urls_count = 0
user_mention_count = 0
symbol_count = 0


dict = {}
dict_sort = []

date_dict = {}

country_dict = {}
country_count = 0

with open(FILE) as f:
    for line in f:
        # print "start"
        # print line
        line =  line.split('~~')
        date = line[0].strip('created_at:')

        # ONLY FOR FAKENEWS, GET TIME
        date = date.split(' ')[1]
        # FOR PANAMA PAPERS GET DATE
        # date = date.split(' ')[0]


        # print str(date)
        tweet = line[1]
        country = line[2].strip("country:")
        entities = line[3].strip('entities:')
        # print entities
        geotag = line[4].strip('geotag:')
        tweet = tweet.strip('tweet:')
        out = "".join(c for c in tweet if c not in ('!', '.',',', ':','?','"','\'','/','(',')'))
        # print out
        # print tweet

        # ENTITIES FINDING
        # print "1 = photo, 2 = urls, 3 = user mention, 4 = symbols"
        if entities != "":
            for a in entities:
                if a == '1':
                    photos_count+=1
                elif a == '2':
                    urls_count+=1
                elif a == '3':
                    user_mention_count+=1
                elif a == '4':
                    symbol_count +=1

        # GEOTAGGED TWEETS COUNTER
        if geotag != '\n':
            print geotag
            geotag_counter+=1

        # FOR FINDING COUNTRIES
        list = out.split(' ')
        if country != "":
            country_count+=1
            # print country
            if country == 'Eastern Time (US & Canada)' or country == 'Pacific Time (US & Canada)' or country == 'Central Time (US & Canada)' or country == 'Mountain Time (US & Canada)':
                country = 'United States of America'
            elif country == 'Atlantic Time (Canada)':
                country = 'Canada'
                # print 'YE DEKH####################'


            if country in country_dict:
                country_dict[country] += 1
            else:
                country_dict[country] = 1
        country_dict_sort = sorted(country_dict.items(), key=operator.itemgetter(1), reverse=True)

        # print country_dict_sort


        # ONLY FOR FAKE NEWS SINCE ALL THE TWEETS ARE SAME DAY
        # MAKE INTERVALS
        time0 = '00:59:59'
        time1 = '02:59:59'
        time2 = '04:59:59'
        time3 = '06:59:59'
        time4 = '08:59:59'

        date = str(date)
        time_key = ''
        if date<time0:
            time_key = 'before 1 pm'
            # print 'below time0',time_key
        elif date>time0 and date<time1:
            time_key = '1 to 3 pm'
            # print 'btw 0 and 1',time_key
        elif date>time1 and date<time2:
            time_key = '3 to 5 pm'
            # print 'btw 1 and 2'
        elif date>time2 and date<time3:
            time_key = '5 to 7 pm'
            # print 'btw 2 and 3'
        elif date>time3 and date<time4:
            time_key = '7 to 9 pm'
            # print 'btw 3 and 4'
        else:
            time_key = '9 pm onwards'
            # print 'greater than 4'
        if time_key in date_dict:
            date_dict[time_key] += 1
        else:
            date_dict[time_key] = 1

        # FOR NORMAL DATE TIME SERIES
        # date = str(date)
        # if date in date_dict:
        #     date_dict[date] +=1
        # else:
        #     date_dict[date] = 1



        # FOR MOST OCCURRING WORDS
        for word in list:
            word = word.lower()
            if not word.startswith('https'):
                if word not in stop_words:
                    # print word
                    if word in dict:
                        dict[word] +=1
                    else:
                        dict[word] = 1
        dict_sort = sorted(dict.items(), key=operator.itemgetter(1),reverse=True)

# GEOTAG TWEETS COUNT PRINTED

# print "geotagged tweets were ",geotag_counter



# PHOTOS ANALYSIS COUNT PIECHART
# print photos_count, urls_count, user_mention_count, symbol_count
analysis_labels = []
analysis_values = []

analysis_labels.append('photos')
analysis_labels.append('urls')
analysis_labels.append('user mention')
analysis_labels.append('symbols')

analysis_values.append(photos_count)
analysis_values.append(urls_count)
analysis_values.append(user_mention_count)
analysis_values.append(symbol_count)

trace = go.Pie(labels=analysis_labels, values=analysis_values)

py.plot([trace], filename='PSOSM_'+OUTPUT+'_photoanalysis')

# Time series graph



# DATE TIMESERIES PLOT

print date_dict
date_list = []
count_list = []
for date_cur, tweet_count in date_dict.iteritems():
    # print date_cur, tweet_count
    # print date_cur > '03:13:33'
    date_list.append(date_cur)
    count_list.append(tweet_count)

data = [go.Scatter(x=date_list, y=count_list,mode='markers')]

py.plot(data, filename='PSOSM_'+OUTPUT+'_timeseries')



# BARGRAPH 20 WORDS

print dict_sort[:20]
# print dict_sort
wordlist = []
freq = []
for a in dict_sort:
    wordlist.append(a[0])
    freq.append(a[1])
    # print a[0],a[1]
data = [go.Bar(
    x=wordlist[:20],
    y=freq[:20]
)]

py.plot(data, filename='PSOSM_'+OUTPUT+'_top_20')


# COUNTRY PIECHART

labels = []
values = []
for country in country_dict_sort:
    labels.append(country[0])
    values.append(country[1])

trace = go.Pie(labels=labels, values=values)

py.plot([trace], filename='PSOSM_'+OUTPUT+'_places')

# Time series graph
