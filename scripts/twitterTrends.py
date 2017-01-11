
import tweepy
import re
import pandas as pd
import config as c
import databaseFunction as d
import inputData as i
from temp import TwitterClient

#global lists
df = pd.DataFrame()
locations = []
woeids = []
created_ats = []
trendStarts = []
trendnames = []
tweet_volumes = []


def clean_tweet(tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def createLists(location, woeid, created_at, trendStart, trendname, tweet_volume):
    locations.append(location)
    woeids.append(woeid)
    created_ats.append(created_at)
    trendStarts.append(trendStart)
    trendnames.append(trendname)
    tweet_volumes.append(tweet_volume)


def createDF(count):

    df['location'] = locations
    df['woeid'] = woeids
    df['created_at'] = created_ats
    df['trendStart'] = trendStarts
    df['trendname'] = trendnames
    df['tweet_volume'] = tweet_volumes
    #print df.sort(['tweet_volume'], ascending=False).groupby(['location']).head(count)
    print "Twitter Trends Calls"

def testing(now):
    twitterTrends(i.woeidList,now)
    print "TwitterTrends Downloads complete"
    #createDF(counter)
    #return df

def twitterTrends(woeidList,now):
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
                    trendname=clean_tweet(trendname)
                    tweet_volume = trendData["tweet_volume"]
                    url = trendData["url"]
                    # print trendname                                   s
                    cur.execute('INSERT INTO twitterTrends(location,woeid,created_at,trendStart,trendname,tweet_volume,timeNow)  VALUES (%s,%s,%s,%s,%s,%s,%s)',
                               (locationData, i, created_at, trendStart, trendname, tweet_volume,now))
                    cc.commit()
                    createLists(locationData, i, created_at, trendStart, trendname, str(tweet_volume))
        break

    cc.close()
# to run trends

#print testing(10)
