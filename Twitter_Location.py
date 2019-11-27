#!/usr/bin/env python
# coding: utf-8

# ## Word Cloud for Sentiment Analysis

# In[1]:

#libraries

import os
import re
import tweepy as tw
import pandas as pd
from sqlalchemy import create_engine
from datetime import date, timedelta, datetime
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# In[2]:

#access keys

consumer_key= 'xxxxxxxxl0VJAJSp9Ob4xxxxxx'
consumer_secret= 'xxxxxBx1InIFRtdOEIJGxvx2Mxxx'
access_token= 'xxxxmLD5g4aEDppJUD3ghn9xxxxxx'
access_token_secret= 'xxxxxxXflBur7pq4SbqwxYZR9vwDcxxxxx'

#auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth = tw.AppAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)


# In[3]:

#defining topic,timeframe for tweet collection

yesterday = date.today() - timedelta(days=1)
today = date.today()

search_words = "TheJoker OR TheJokerFILM OR JokerFilm OR TheJOKERmovie OR jokermovie" + " -filter:retweets"
date_since = "2019-10-08"
date_until = "2019-10-10"


# In[4]:


tweets = tw.Cursor(api.search,
                       q=search_words,
                       since=date_since,
                       until=today,
                       result_type="recent",
                        tweet_mode="extended").items(2000)

users_locs = [[tweet.user.name, tweet.lang, tweet.user.location, tweet.coordinates, tweet.created_at,tweet.favorite_count,tweet.retweet_count,tweet.user.followers_count,tweet.user.verified, tweet.full_text] for tweet in tweets]


# In[5]:

#constructing Data Frame


twitter_data = pd.DataFrame(data=users_locs,columns=['username','language','location', 'coordinates','created_at',
                                                     'favorite_count','retweet_count','followers','verified','text'])

twitter_data['created_at'] = twitter_data['created_at'] + timedelta(hours=2)

twitter_data = twitter_data[['username','language','location','coordinates','created_at','favorite_count',
                             'retweet_count','followers','verified','text']]


# In[6]:

#cleaning twitter text


def remove_name_and_link(w):
  return   ' '.join(re.sub("(@[A-Za-z0-9]+) | (\nhttps?://[A-Za-z0-9./]*) |(https?://[A-Za-z0-9./]*)| (//t.[A-Za-z0-9./]*) | (RT @[\w]*:) |(@[\w]*)"," ",w).split())

twitter_data['text_clean'] = twitter_data['text'].apply(remove_name_and_link)

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

twitter_data = twitter_data[['created_at','username','verified','location','coordinates','language','favorite_count','retweet_count','followers','compound','positive','neutral','negative','text','text_clean']]


# In[7]:

#categorize tweet sentiment

def sentiment_analyzer(w):
     if w >= 0.05:
            return "positive"
     elif (w < 0.05) and (w > -0.05):
            return "neutral"
     else:
            return "negative"

        
twitter_data['general_sen'] = twitter_data['compound'].apply(sentiment_analyzer)


# In[42]:


#export_csv = twitter_data.to_csv (r'C:\\Users\\User\twitlocati.csv', index = True, header=True,sep=";") 


# In[272]:


twitter_data=  pd.read_excel('canadaloc.xlsx')


# In[291]:


df = twitter_data.iloc[0:1000]


# ### Detect Coordinates from Location String

# In[293]:


from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="st3553ggd")

from geopy.extra.rate_limiter import RateLimiter
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=2)


# In[294]:


def geo_location(item):

    try:
        language = geolocator.geocode(item)
        return(language.latitude,language.longitude)
    except:
        return


# In[ ]:


df['coordinates'] = df['language'].apply(geo_location)


# In[296]:


len(df['coordinates'].unique())


# In[176]:


df1 = df.copy()
#df2 = df.copy()
#df3 = df.copy()
#df4 = df.copy()
#df5 = df.copy()
#df6 = df.copy()
#df7 = df.copy()
#df8 = df.copy()
#df9 = df.copy()
#df10 = df.copy()
#df11 = df.copy()
#df12 = df.copy()
#df13 = df.copy()
#df14 = df.copy()
#df15 = df.copy()
#df16 = df.copy()


# In[177]:


mydf = [df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,df14,df15,df16]


# In[178]:


result = pd.concat(mydf)


# In[179]:


result = result[result.location !="NaN"]


# In[195]:



result['location'] = result['location'].astype(str)


# In[201]:


for item in result['location']:
    if (item == 'NaN'):
        print(item)


# In[210]:


backup = result


# In[211]:


result.dropna(subset=['location'], how = 'any',inplace = True)


# In[222]:


l= []

for i, item in enumerate(result.location):
    if (item == 'nan'):
        l.append(i)
        


# In[247]:


result.index = list(range(0,16000,1))


# In[243]:


result = result.drop(columns = ['Unnamed: 0'])


# In[249]:


r = result.drop(labels = l, inplace = False)


# In[269]:


r['coordinates'].dropna(inplace=True)


# In[267]:


#Save file in csv format

export_csv = r.to_csv (r'C:\\Users\\User\twitterlocation.csv', index = True, header=True,sep=";") 

