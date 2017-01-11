from datetime import datetime
import twitterTrends as tT
import databaseFunction as d
import temp as t

cc = d.sqlConnection()
cur = cc.cursor()

class TwitterTrendAnalysis:
    def __init__(self):
        print "This is TTA CLASS"
    def getLatestTrends(self):
        now = datetime.now().strftime('%Y-%m-%d %H:') + '%'
        tT.testing(now)
    def getTrendsOFTweets(self):
        count=5
        now = datetime.now().strftime('%Y-%m-%d %H:') + '%'
        cur.execute("select t.trendname,t.tweet_volume from twitterTrends t inner join locationName l on l.location=t.location where t.timeNow LIKE '%s' order by t.tweet_volume desc limit 30;" % now);
        data = cur.fetchall()
        for q in data:
            client = t.TwitterClient(q[0])
            client.get_tweets(count)
        self.getEstimation(data,count)

    def getEstimation(self,data,count):
        #hastag
        for i in data:
            print i[0]
            cur.execute("create view tags as select tag,count(tag) as tagcount from twitterSearch where hashtag='%s' group by tag ORDER BY tagcount desc"%(i[0]));
            cc.commit()
            cur.execute("select * from tags ORDER BY tagcount DESC limit 1")
            tagslist = cur.fetchall()
            for f in tagslist:
                active= float(f[1])/count
                result= float(i[1]) * active
                sql="update twitterTrends set tag=%s,typeTweets=%s WHERE trendname=%s"
                cur.execute(sql,(f[0],str(result),i[0]))
                cc.commit()
            cur.execute("drop view tags")
            cc.commit()

def caller():
    tta = TwitterTrendAnalysis()
    tta.getLatestTrends()
    tta.getTrendsOFTweets()


if __name__ == '__main__':

