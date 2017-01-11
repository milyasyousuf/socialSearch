import MySQLdb
from scripts import databaseFunction as d,temp as t
from datetime import datetime

cc = d.sqlConnection()
cur = cc.cursor()
def worker(query):
        clinet = t.TwitterClient(query)
        clinet.get_tweets(30)
        #print "tests"
        cur.execute("select  tweet,tweetLang,tweetUser,create_at,tag from twitterSearch WHERE hashtag='%s';"%query)
        #print ("select  tweet,tweetLang,tweetUser,create_at from twitterSearch WHERE qureyTime=%d;"%query)
        data = cur.fetchall()
        return data

def getTwitterTrends():
        now=datetime.now().strftime('%Y-%m-%d %H:')+'%'
        print now
        #df = tT.testing(now)
        cur.execute("select t.trendname,t.tweet_volume,t.trendStart,t.location,t.tag,t.typeTweets from twitterTrends t inner join locationName l on l.location=t.location where t.timeNow LIKE '%s' order by t.tweet_volume desc limit 30;"%now);
        data=cur.fetchall()
        #print data
        #print "\n\n\n\n\n\n\n"
        return data

