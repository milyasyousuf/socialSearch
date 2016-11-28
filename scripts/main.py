import Queue
import threading
import urllib2
import youtube as y
import databaseFunction as d
import twitterTrends as tT

def maintainYoutube(query,count):
  y.argparser.add_argument("--q", default=query)
  y.argparser.add_argument("--max-results", help="Max results", default=count)
  args = y.argparser.parse_args()

  try:
    df = y.youtube_search(args)
  except y.HttpError, e:
    print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)
  return df

# called by each thread
def get_url(q, url):
    q.put(urllib2.urlopen(url).read())

def printing(u):
  print u


#theurls = ["http://google.com", "http://yahoo.com"]

#q = Queue.Queue()
#t = threading.Thread(target=get_url, args = (q,u))
#for u in theurls:
#	t=threading.Thread(printing(u))
#	t.daemon = True
#   	t.start()

#s = q.get()
#print s
if __name__ == "__main__":
  print "test"
  #  df = maintainYoutube("google",10)
    #con = d.sqlConnection()
  df = tT.testing(10)
  print df['trendname']