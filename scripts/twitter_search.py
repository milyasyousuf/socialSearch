#!/usr/bin/python

from tweepy import Stream
from tweepy.auth import OAuthHandler
from tweepy.streaming import StreamListener
from progressbar import ProgressBar, Percentage, Bar
import json
import config as c
import pandas as pd
import databaseFunction as d
import sys
#from pymongo import MongoClient

tweetList = []
tweetId = []
tweetCreated_at = []
tweetLang = []
tweetPlace = []
tweetUser = []
tweetUserId=[]
#tweetUserLang =[]
d1=pd.DataFrame()
cc = d.sqlConnection()
cur = cc.cursor()
max_tweets =1
qt=""

def createLists(data_file):
    tweetList.append(data_file['text'].encode('utf-8'))
    tweetId.append(data_file['id'])
    tweetCreated_at.append(data_file['created_at'])
    tweetLang.append(data_file['lang'])
    tweetPlace.append(data_file['place'])
    tweetUser.append(data_file['user']['name'].encode('utf-8'))
    tweetUserId.append(data_file['user']['id'])

    cur.execute('INSERT INTO twitterSearch(tweet,create_at,tweetLang,tweetUser,tweetUserId,queryTime)  VALUES (%s,%s,%s,%s,%s,%s)',
        (data_file['text'],data_file['created_at'],data_file['lang'],data_file['user']['name'].encode('utf-8'),data_file['user']['id'],qt))
    cc.commit()
    print "call lists"

def createDf():
    print "DF call"
    d1['tweets']=tweetList
    d1['created_at']=tweetCreated_at
    d1['tweetLang'] = tweetLang
    d1['tweetUser'] = tweetUser
    d1['tweetUserId'] = tweetUserId




def getDF():
    print "getdf call"
    return d1
def getTweets(query):
	#qt=queryTime
    #Get the OAuth token
    	auth = OAuthHandler(c.consumer_key, c.consumer_secret)
    	auth.set_access_token(c.access_token, c.access_token_secret)
        #Use the listener class for stream processing
    	twitterStream = Stream(auth, listener())
        #Filter for these topics
    	twitterStream.filter(track=[query])

"""
def insertIntoMongo(data):
    client = MongoClient('localhost', 27017)
    db = client['tweets']
    collection = db['twitter_collection']
    collection.insert(data)
    return True
"""
#Create the listener class that will receive and save tweets
class listener(StreamListener):

    #On init, set the counter to zero and create a progress bar
    def __init__(self, api=None):
	self.num_tweets = 0
	self.pbar = ProgressBar(widgets=[Percentage(), Bar()], maxval=max_tweets).start()

    #When data is received, do this
    def on_data(self, data):
	data_file = json.loads(data)
        print "call"
        createLists(data_file)
        #print data_file['user']['lang']
        #print data_file['user']['location']
            #insertIntoMongo(data_file)
	    #data_file = json.dumps(data,indent=4)
	    #Increment the number of tweets
	self.num_tweets += 1
            #Check to see if we have hit max_tweets and exit if so
	if self.num_tweets >= max_tweets:
		self.pbar.finish()
                #createDf()
               	sys.exit(0)
        else:
                #increment the progress bar
		self.pbar.update(self.num_tweets)
	return True

    #Handle any errors that may occur
    def on_error(self, status):
        print status


# The number of tweets we want to get
if __name__ == '__main__':
    getTweets(sys.argv[1])

