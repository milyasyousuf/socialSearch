#!/usr/bin/python
# -*- coding: utf-8 -*-
import tweepy
import MySQLdb
import pandas as pd
import config as c
import databaseFunction as d
import inputData as i

#global lists
df = pd.DataFrame()
locations = []
woeids = []
created_ats = []
trendStarts = []
trendnames = []
tweet_volumes = []


def createLists(location, woeid, created_at, trendStart, trendname, tweet_volume):
    locations.append(location)
    woeids.append(woeid)
    created_ats.append(created_at)
    trendStarts.append(trendStart)
    trendnames.append(trendname)
    tweet_volumes.append(tweet_volume)


def createDF(count):
    twitterTrends(i.woeidList)
    df['location'] = locations
    df['woeid'] = woeids
    df['created_at'] = created_ats
    df['trendStart'] = trendStarts
    df['trendname'] = trendnames
    df['tweet_volume'] = tweet_volumes
    #print df.sort(['tweet_volume'], ascending=False).groupby(['location']).head(count)
    print "Twitter Trends Calls"

def testing(counter):
    createDF(counter)
    return df

def twitterTrends(woeidList):
    # OAuth process, using the keys and tokens
    auth = tweepy.OAuthHandler(c.consumer_key, c.consumer_secret)
    auth.set_access_token(c.access_token, c.access_token_secret)
    api = tweepy.API(auth)
    woeidList=woeidList
    cc = d.sqlConnection()
    cur = cc.cursor()

    for i in woeidList:
        print i
        trends1 = api.trends_place(i)
        # conn.commit
        for data in trends1:
            location = data["locations"]
            for j in location:
                locationData = j['name']

                trendsList = data["trends"]
                created_at = data["created_at"]
                trendStart = data["as_of"]
                # print locationData["name"]
                #print locationData
                #print trendStart
                #print created_at
                for trendData in trendsList:
                    trendname = trendData["name"].encode('utf-8')
                    tweet_volume = trendData["tweet_volume"]
                    url = trendData["url"]
                    # print trendname                                   s
                    print tweet_volume

                    cur.execute('INSERT INTO twitterTrends(location,woeid,created_at,trendStart,trendname,tweet_volume)  VALUES (%s,%s,%s,%s,%s,%s)',
                               (locationData, i, created_at, trendStart, trendname, tweet_volume))
                    cc.commit()
                    createLists(locationData, i, created_at, trendStart, trendname, str(tweet_volume))
        break

    cc.close()
# to run trends

#print testing(10)