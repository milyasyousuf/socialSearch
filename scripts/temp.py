# author = rhnvrm <hello@rohanverma.net>

import os
import re,json
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
import databaseFunction as d
import config as c


cc = d.sqlConnection()
cur = cc.cursor()


def createLists(text, created_at, lang, user, userid,qt):
    # print data.user.id
    cur.execute(
        'INSERT INTO twitterSearch(tweet,create_at,tweetLang,tweetUser,tweetUserId,queryTime)  VALUES (%s,%s,%s,%s,%s,%s)',
        (text.encode('utf-8'), created_at, lang, user.encode('utf-8'), userid, qt))
    cc.commit()
    print "call lists"

class TwitterClient(object):
    '''
    Generic Twitter Class for the App
    '''

    def __init__(self, query, retweets_only=False, with_sentiment=False):
        # keys and tokens from the Twitter Dev Console
        consumer_secret = c.consumer_secret
        consumer_key = c.consumer_key
        access_token = c.access_token
        access_token_secret = c.access_token_secret

        # Attempt authentication
        try:
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            self.auth.set_access_token(access_token, access_token_secret)
            self.query = query
            self.retweets_only = retweets_only
            self.with_sentiment = with_sentiment
            self.api = tweepy.API(self.auth)
            self.tweet_count_max = 10  # To prevent Rate Limiting
        except:
            print("Error: Authentication Failed")

    def set_query(self, query=''):
        self.query = query

    def set_retweet_checking(self, retweets_only='false'):
        self.retweets_only = retweets_only

    def set_with_sentiment(self, with_sentiment='false'):
        self.with_sentiment = with_sentiment

    def clean_tweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def get_tweet_sentiment(self, tweet):
        analysis = TextBlob(self.clean_tweet(tweet))
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'



    def get_tweets(self):
        tweets = []

        try:
            recd_tweets = self.api.search(q=self.query,
                                          count=self.tweet_count_max)
            if not recd_tweets:
                pass
            for data in recd_tweets:
                parsed_tweet = {}

                #parsed_tweet['text'] = tweet.text
                #parsed_tweet['user'] = tweet.user.screen_name
                test= self.query
                #print tweet.user.id
                tweet = self.clean_tweet(data.text)

                createLists(tweet,data.created_at,data.lang,data.user.screen_name,data.user.id,test)
                #print json.dumps(tweet,indent=5)

                #if self.with_sentiment == 1:
                 #   parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)
                #else:
                 #   parsed_tweet['sentiment'] = 'unavailable'

                #if tweet.retweet_count > 0 and self.retweets_only == 1:
                #    if parsed_tweet not in tweets:
                 #       tweets.append(parsed_tweet)
                #elif not self.retweets_only:
                 #   if parsed_tweet not in tweets:
                  #      tweets.append(parsed_tweet)

            return tweets

        except tweepy.TweepError as e:
            print("Error : " + str(e))



