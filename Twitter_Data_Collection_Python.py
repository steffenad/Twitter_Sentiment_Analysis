#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#import libraries

import os
import re
import tweepy as tw
import pandas as pd
from sqlalchemy import create_engine
from datetime import date, timedelta, datetime
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#access to Twitter APIs

consumer_key= 'xxxpejEeRjl0VJAJSp9Ob4xxx'
consumer_secret= 'xxxsV4yayNBx1InIFRtdOEIJGxvx2MRawuuoARa5xEe4PIpxxx'
access_token= 'xxx3536113492942849-mM10EmLD5g4aEDppJUD3ghn96nCxxx'
access_token_secret= 'xxxOvLRAiADzQe9CsJXflBur7pq4SbqwxYZR9vwDchxxx'

#auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth = tw.AppAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)

#Collecting tweets about "Trudeau"

yesterday = date.today() - timedelta(days=1)
today = date.today()

search_words = "trudeau" + " -filter:retweets"


tweets = tw.Cursor(api.search,
                       q=search_words,
                       lang='en',
                       since=yesterday,
                       until=today,
                       result_type="recent",
                        tweet_mode="extended").items(200000)

users_locs = [[tweet.user.name, tweet.lang, tweet.user.location, tweet.created_at,tweet.favorite_count,
               tweet.retweet_count,tweet.user.followers_count,
               tweet.user.verified, tweet.full_text] for tweet in tweets]

pd.set_option('display.max_colwidth', 280)

#build data frame
twitter_data = pd.DataFrame(data=users_locs,columns=['username','language','location','created_at',
                                                     'favorite_count','retweet_count','followers','verified',
                                                     'text'])

#sort columns
twitter_data = twitter_data[['username','language','location','created_at','favorite_count','retweet_count',
                             'followers','verified','text']]



#Cleaning text

def remove_name_and_link(w):
  return   ' '.join(re.sub("(@[A-Za-z0-9]+) | (\nhttps?://[A-Za-z0-9./]*) |(https?://[A-Za-z0-9./]*)|(//t.[A-Za-z0-9./]*) | (RT @[\w]*:) |(@[\w]*)"," ",w).split())

twitter_data['text_clean'] = twitter_data['text'].apply(remove_name_and_link)



#Sentiment Analysis

analyser = SentimentIntensityAnalyzer()

def sentiment_analyzer_scores(sentence):
     score = analyser.polarity_scores(sentence)
     print(score)

tweet = []
compound = []
positive = []
neutral = []
negative = []

for i in range(0, len(twitter_data)):
    tweet.append(twitter_data['text_clean'][i])
    compound.append(analyser.polarity_scores(twitter_data['text_clean'][i])['compound'])
    positive.append(analyser.polarity_scores(twitter_data['text_clean'][i])['pos'])
    neutral.append(analyser.polarity_scores(twitter_data['text_clean'][i])['neu'])
    negative.append(analyser.polarity_scores(twitter_data['text_clean'][i])['neg'])
 

twitter_data['compound']=compound
twitter_data['positive']=positive
twitter_data['neutral']=neutral
twitter_data['negative']=negative

twitter_data = twitter_data[['created_at','username','verified','location','language','favorite_count',
                             'retweet_count','followers','compound','positive','neutral','negative',
                             'text','text_clean']]



#Categorize Sentiment into 3 classes

def sentiment_analyzer(w):
     if w >= 0.05:
            return "positive"
     elif (w < 0.05) and (w > -0.05):
            return "neutral"
     else:
            return "negative"

        
twitter_data['general_sen'] = twitter_data['compound'].apply(sentiment_analyzer)



#Store Data on SQL Google Cloud

engine = create_engine("mysql+pymysql://{user}:{pw}@35.239.145.12:3306/{db}".format(user="username",pw="password",db="twitterdb"))

twitter_data.to_sql('canada', con = engine, if_exists = 'append', index=False)



#Twitter Data Collection for "Scheer"



search_words = "scheer" + " -filter:retweets"

tweets = tw.Cursor(api.search,
                       q=search_words,
                       lang='en',
                       since=yesterday,
                       until=today,
                       result_type="recent",
                        tweet_mode="extended").items(200000)

users_locs = [[tweet.user.name, tweet.lang, tweet.user.location, tweet.created_at,tweet.favorite_count,
               tweet.retweet_count,tweet.user.followers_count,tweet.user.verified,
               tweet.full_text] for tweet in tweets]

pd.set_option('display.max_colwidth', 280)


twitter_data = pd.DataFrame(data=users_locs,columns=['username','language','location','created_at',
                                                     'favorite_count','retweet_count','followers','verified',
                                                     'text'])


twitter_data = twitter_data[['username','language','location','created_at','favorite_count','retweet_count',
                             'followers','verified','text']]

#Data Cleaning

def remove_name_and_link(w):
  return   ' '.join(re.sub("(@[A-Za-z0-9]+) | (\nhttps?://[A-Za-z0-9./]*) |(https?://[A-Za-z0-9./]*)| (//t.[A-Za-z0-9./]*) | (RT @[\w]*:) |(@[\w]*)"," ",w).split())

twitter_data['text_clean'] = twitter_data['text'].apply(remove_name_and_link)



#Sentiment Analysis

analyser = SentimentIntensityAnalyzer()

def sentiment_analyzer_scores(sentence):
     score = analyser.polarity_scores(sentence)
     print(score)

tweet = []
compound = []
positive = []
neutral = []
negative = []

for i in range(0, len(twitter_data)):
    tweet.append(twitter_data['text_clean'][i])
    compound.append(analyser.polarity_scores(twitter_data['text_clean'][i])['compound'])
    positive.append(analyser.polarity_scores(twitter_data['text_clean'][i])['pos'])
    neutral.append(analyser.polarity_scores(twitter_data['text_clean'][i])['neu'])
    negative.append(analyser.polarity_scores(twitter_data['text_clean'][i])['neg'])
 

twitter_data['compound']=compound
twitter_data['positive']=positive
twitter_data['neutral']=neutral
twitter_data['negative']=negative

twitter_data = twitter_data[['created_at','username','verified','location','language','favorite_count',
                             'retweet_count','followers','compound','positive','neutral','negative','text',
                             'text_clean']]


#categorize sentiment into 3 classes

def sentiment_analyzer(w):
     if w >= 0.05:
            return "positive"
     elif (w < 0.05) and (w > -0.05):
            return "neutral"
     else:
            return "negative"

        
twitter_data['general_sen'] = twitter_data['compound'].apply(sentiment_analyzer)



#store data on SQL Google Cloud

engine = create_engine("mysql+pymysql://{user}:{pw}@35.239.145.12:3306/{db}".format(user="username",
                                                                                    pw="password",db="twitterdb"))

twitter_data.to_sql('canada', con = engine, if_exists = 'append', index=False)




search_words = "TheJoker OR TheJokerFILM OR JokerFilm OR TheJOKERmovie OR jokermovie" + " -filter:retweets"


tweets = tw.Cursor(api.search,
                       q=search_words,
                       lang='en',
                       since=yesterday,
                       until=today,
                       result_type="recent",
                        tweet_mode="extended").items(200000)

users_locs = [[tweet.user.name, tweet.lang, tweet.user.location, tweet.created_at,tweet.favorite_count,
               tweet.retweet_count,tweet.user.followers_count,tweet.user.verified,
               tweet.full_text] for tweet in tweets]

pd.set_option('display.max_colwidth', 280)


twitter_data = pd.DataFrame(data=users_locs,columns=['username','language','location','created_at',
                                                     'favorite_count','retweet_count','followers','verified',
                                                     'text'])


twitter_data = twitter_data[['username','language','location','created_at','favorite_count','retweet_count',
                             'followers','verified','text']]



#Clean Data

def remove_name_and_link(w):
  return   ' '.join(re.sub("(@[A-Za-z0-9]+) | (\nhttps?://[A-Za-z0-9./]*) |(https?://[A-Za-z0-9./]*)| (//t.[A-Za-z0-9./]*) | (RT @[\w]*:) |(@[\w]*)"," ",w).split())

twitter_data['text_clean'] = twitter_data['text'].apply(remove_name_and_link)



#Sentiment Analysis

analyser = SentimentIntensityAnalyzer()

def sentiment_analyzer_scores(sentence):
     score = analyser.polarity_scores(sentence)
     print(score)

tweet = []
compound = []
positive = []
neutral = []
negative = []

for i in range(0, len(twitter_data)):
    tweet.append(twitter_data['text_clean'][i])
    compound.append(analyser.polarity_scores(twitter_data['text_clean'][i])['compound'])
    positive.append(analyser.polarity_scores(twitter_data['text_clean'][i])['pos'])
    neutral.append(analyser.polarity_scores(twitter_data['text_clean'][i])['neu'])
    negative.append(analyser.polarity_scores(twitter_data['text_clean'][i])['neg'])
 

twitter_data['compound']=compound
twitter_data['positive']=positive
twitter_data['neutral']=neutral
twitter_data['negative']=negative

twitter_data = twitter_data[['created_at','username','verified','location','language','favorite_count',
                             'retweet_count','followers','compound','positive','neutral','negative','text',
                             'text_clean']]


#categorize sentiment into 3 classes

def sentiment_analyzer(w):
     if w >= 0.05:
            return "positive"
     elif (w < 0.05) and (w > -0.05):
            return "neutral"
     else:
            return "negative"

        
twitter_data['general_sen'] = twitter_data['compound'].apply(sentiment_analyzer)

engine = create_engine("mysql+pymysql://{user}:{pw}@35.239.145.12:3306/{db}".format(user="username",
                                                                                    pw="password",db="twitterdb"))

twitter_data.to_sql('thejoker', con = engine, if_exists = 'append', index=False)


