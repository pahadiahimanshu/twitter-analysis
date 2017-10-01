# Twitter Analysis
Project aims to explore the tweepy library for python to extract data on certain hashtags and make inferences from the results.
#### End goals - 
* Collecting tweets for Hashtags - #PanamaPapers and #FakeNews
    * Histogram - Top 20 most frequently occuring words in tweets
    * Pie Chart - % of tweets from each country
    * Time series graph (x: time or date, y: number of tweets)
    * Pie Chart - Analyze the content of the tweets (Images, URLs, User-mention, Symbols)
* Get the first tweet of any user

### Understanding code files

* Collect-tweet.py - Collects the tweets and saves it to txt file
    * Use your own application's consumer key, consumer_secret, access_token and access_token_secret
    * Change the hashtag variable
    * This program takes care of the twitter rate limiting by making itself sleep for 15 mins when the API limit is reached
* tweet-parser.py - Parse the database text file and plot the graphs mentioned in end goals
* user-first-tweet.py - Explores the user's timeline and extracts out his first tweet.
    * Doesn't work for large number of tweets


### Tech

Project uses - 

* [Python] 
* [Tweepy] - Twitter python library 
* [NLTK] - Natural language toolkit
* [PLotly] - Tool for plotting graphs, pie charts - requires internet connection (You canuse [matplotlib] also)


### Todos

 - Add the plots and inferences to the README file


   [Python]: <https://www.python.org/>
   [tweepy]: <http://www.tweepy.org/>
   [NLTK]: <http://www.nltk.org/>
   [Plotly]: <https://plot.ly/python/>
   [matplotlib]: <https://matplotlib.org/>