import MySQLdb
from scripts import databaseFunction as d,temp as t


def worker(query):
        clinet = t.TwitterClient(query)
        clinet.get_tweets()
        print "tests"
        cc = d.sqlConnection()
        cur = cc.cursor()
        cur.execute("select  tweet,tweetLang,tweetUser,create_at from twitterSearch WHERE queryTime='%s';"%query)
        #print ("select  tweet,tweetLang,tweetUser,create_at from twitterSearch WHERE qureyTime=%d;"%query)
        data = cur.fetchall()
        return data
