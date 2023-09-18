#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install git+https://github.com/JustAnotherArchivist/snscrape.git')


# In[1]:


import snscrape.modules.twitter as sntwitter
import pandas as pd


# In[14]:


def tweets(username,since,upto,maxtweets):
    maxTweets = maxtweets
    tweets_list = []

# Using TwitterSearchScraper to scrape data and append tweets to list
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:{0} since:{1} until:{2}'.format(username,since,upto)).get_items()):
        if i>maxTweets:
            break
        tweets_list.append([tweet.date, tweet.id, tweet.rawContent, tweet.user.username])
    tweets_df = pd.DataFrame(tweets_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
    tweets_df.to_csv('{0}.csv'.format(username), sep=',', index=False)
    return tweets_df


# In[17]:


#tweets('TimesNow','2023-05-01','2023-05-31',10000)


# In[ ]:




