# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 05:17:55 2020

@author: Shih-Yuan Wang
"""

## import the libraries
import tweepy, codecs, os, sys, csv
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

## fill in Twitter credentials 
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

#--------------------------------------------------------------------------------
# Get Uber Tweets
#--------------------------------------------------------------------------------

## let Tweepy set up an instance of the REST API
auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
#api = tweepy.API(auth)
#Maximum number of tweets we want to collect 
maxTweets = 100000

#The twitter Search API allows up to 100 tweets per query
tweetsPerQry = 100
searchQuery = ('Uber')
tweetCount = 0
#http://www.dealingdata.net/2016/07/23/PoGo-Series-Tweepy/
#https://pastebin.com/9rC7UrVn
## use the codecs library to write the text of the Tweets to a .txt file

#Old way of doing things - which is what you will see a lot of people doing online
max_id = -1
tweetCount = 0
with codecs.open("twitterOut_Uber.csv", "w", "utf-8") as file:
    #While we still want to collect more tweets
    while tweetCount < maxTweets:
        try:
            #Look for more tweets, resuming where we left off
            if max_id <= 0:
                new_tweets = api.search(q=searchQuery, lang = "en", count=tweetsPerQry)
            else:
                new_tweets = api.search(q=searchQuery, lang = "en", count=tweetsPerQry, max_id=str(max_id - 1))
            
            #If we didn't find any exit the loop
            if not new_tweets:
                print("No more tweets found")
                break
            
            for tweet in new_tweets:
                #Make sure the tweet has place info before writing
                #if (tweet.geo is not None) and (tweetCount < maxTweets):
                if (tweetCount < maxTweets):
                    if (len(tweet.id_str)==0):
                        file.write(" ")
                    else :
                        file.write(tweet.id_str)
                    file.write("\t")
                    if (len(str(tweet.user.id))==0):
                        file.write(" ")
                    else :
                        file.write(str(tweet.user.id))
                    file.write("\t")
                    file.write(str(tweet.user.location))
                    file.write("\t")
                    
                    file.write(str(tweet.created_at))
                    file.write("\t'")
                    file.write(str(tweet.text.encode('utf-8')))
                    file.write("\t")
                    #ss = p.clean(str(tweet.text.encode('utf-8')))
                    #file.write(ss)
                    #file.write("\t")
                    
                    #Choose one of the two analysis that fit what you need
                    #default sentiment analysis
                    tt = TextBlob(str(tweet.text.encode('utf-8')))
                    #tt = TextBlob(ss)
                    file.write(str(tt.sentiment.polarity))
                    file.write("\t")
                    file.write(str(tt.sentiment.subjectivity))
                    file.write("\t")
                    
                    #if you using NaiveBayes
                    #tt2 = TextBlob(str(tweet.text.encode('utf-8')), analyzer=NaiveBayesAnalyzer())
                    #tt2 = TextBlob(ss, analyzer=NaiveBayesAnalyzer())
                    #file.write(str(tt2.sentiment.classification))
                    #file.write("\t")
                    #file.write(str(tt2.sentiment.p_pos))
                    #file.write("\t")
                    #file.write(str(tt2.sentiment.p_neg))
                    
                    file.write("\n")
                    
                    #tt=TextBlob(str(tweet.text.encode('utf-8')), )
                    tweetCount += 1
                    
            #Display how many tweets we have collected
            print("Downloaded {0} tweets".format(tweetCount))
            
            #Record the id of the last tweet we looked at
            max_id = new_tweets[-1].id
            
        except tweepy.TweepError as e:
            
            #Print the error and continue searching
            print("some error : " + str(e))

file.close()

#--------------------------------------------------------------------------------
# Get Lyft Tweets
#--------------------------------------------------------------------------------

## let Tweepy set up an instance of the REST API
auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
#api = tweepy.API(auth)
#Maximum number of tweets we want to collect 
maxTweets = 100000

#The twitter Search API allows up to 100 tweets per query
tweetsPerQry = 100
searchQuery = ('Lyft')

tweetCount = 0
#http://www.dealingdata.net/2016/07/23/PoGo-Series-Tweepy/
#https://pastebin.com/9rC7UrVn
## use the codecs library to write the text of the Tweets to a .txt file

#Old way of doing things - which is what you will see a lot of people doing online
max_id = -1
tweetCount = 0
with codecs.open("twitterOut_Lyft.csv", "w", "utf-8") as file:
    #While we still want to collect more tweets
    while tweetCount < maxTweets:
        try:
            #Look for more tweets, resuming where we left off
            if max_id <= 0:
                new_tweets = api.search(q=searchQuery, lang = "en", count=tweetsPerQry)
            else:
                new_tweets = api.search(q=searchQuery, lang = "en", count=tweetsPerQry, max_id=str(max_id - 1))
            
            #If we didn't find any exit the loop
            if not new_tweets:
                print("No more tweets found")
                break
            
            for tweet in new_tweets:
                #Make sure the tweet has place info before writing
                #if (tweet.geo is not None) and (tweetCount < maxTweets):
                if (tweetCount < maxTweets):
                    if (len(tweet.id_str)==0):
                        file.write(" ")
                    else :
                        file.write(tweet.id_str)
                    file.write("\t")
                    if (len(str(tweet.user.id))==0):
                        file.write(" ")
                    else :
                        file.write(str(tweet.user.id))
                    file.write("\t")
                    file.write(str(tweet.user.location))
                    file.write("\t")


                    file.write(str(tweet.created_at))
                    file.write("\t'")
                    file.write(str(tweet.text.encode('utf-8')))
                    file.write("\t")
                    
                    #Choose one of the two analysis that fit what you need
                    #default sentiment analysis
                    tt = TextBlob(str(tweet.text.encode('utf-8')))
                    #tt = TextBlob(ss)
                    file.write(str(tt.sentiment.polarity))
                    file.write("\t")
                    file.write(str(tt.sentiment.subjectivity))
                    file.write("\t")
                                        
                    file.write("\n")
                    
                    #tt=TextBlob(str(tweet.text.encode('utf-8')), )
                    tweetCount += 1
                    
            #Display how many tweets we have collected
            print("Downloaded {0} tweets".format(tweetCount))
            
            #Record the id of the last tweet we looked at
            max_id = new_tweets[-1].id
            
        except tweepy.TweepError as e:
            
            #Print the error and continue searching
            print("some error : " + str(e))

file.close()
