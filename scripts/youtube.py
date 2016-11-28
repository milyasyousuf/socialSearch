from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser
import requests
import json
import threading
import pandas as pd


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "AIzaSyD2vaw0LI02UrPPdGGkDfAAuca9P65I3r8"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def getViews(id):
  url = ("https://www.googleapis.com/youtube/v3/videos?part=snippet%2C+statistics&id="+id+"&maxResults=50&key="+DEVELOPER_KEY)
  response = requests.get(url, timeout=5)
  if response.status_code != 200:
        print("Failed to connect to server " + str(response.status_code))
  else:
        returnObj = json.loads(response.content)
        #print returnObj
        viewCount = str(returnObj['items'][0]['statistics']['viewCount'])
        likeCount = str(returnObj['items'][0]['statistics']['likeCount'])
        dislikeCount = str(returnObj['items'][0]['statistics']['dislikeCount'])
        favoriteCount = str(returnObj['items'][0]['statistics']['favoriteCount'])
        commentsCount = str(returnObj['items'][0]['statistics']['commentCount'])
  return viewCount,likeCount,dislikeCount,favoriteCount,commentsCount



def youtube_search(options):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtube.search().list(
    q=options.q,
    part="id,snippet",
    maxResults= options.max_results
  ).execute()


  videoIds = []
  title = []
  viewCounts = []
  likeCounts = []
  dislikeCounts = []
  favoriteCounts= []
  commentCounts= []
  channels = []
  playlists = []
  publishedTimes = []
  df = pd.DataFrame()

  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
  for search_result in search_response.get("items", []):
    #print json.dumps(search_result,indent=4)
    if search_result["id"]["kind"] == "youtube#video":
      viewCount, likeCount, dislikeCount, favoriteCount, commentsCount=getViews(search_result["id"]["videoId"])
      videoIds.append(search_result["id"]["videoId"])
      title.append(search_result["snippet"]["title"])
      viewCounts.append(viewCount)
      likeCounts.append(likeCount)
      dislikeCounts.append(dislikeCount)
      favoriteCounts.append(favoriteCount)
      commentCounts.append(commentsCount)
      publishedTimes.append(search_result['snippet']['publishedAt'])

    elif search_result["id"]["kind"] == "youtube#channel":
      channels.append("%s (%s)" % (search_result["snippet"]["title"],
                                   search_result["id"]["channelId"]))
    elif search_result["id"]["kind"] == "youtube#playlist":
      playlists.append("%s (%s)" % (search_result["snippet"]["title"],
                                    search_result["id"]["playlistId"]))

  #print "Videos:\n", "\n".join(videos), "\n"
  #print "Channels:\n", "\n".join(channels), "\n"
  #print "Playlists:\n", "\n".join(playlists), "\n"
  df['videoIds']=videoIds
  df['title'] = title
  df['viewCount'] = viewCounts
  df['likeCount'] = likeCounts
  df['dislikeCount'] = dislikeCounts
  df['favoriteCount'] = favoriteCounts
  df['commentCount'] = commentCounts
  df['publishedTime'] = publishedTimes
  return df

"""
if __name__ == "__main__":
  argparser.add_argument("--q", default="Google")
  argparser.add_argument("--max-results", help="Max results", default=)
  args = argparser.parse_args

  try:
    youtube_search(args)
  except HttpError, e:
    print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)"""