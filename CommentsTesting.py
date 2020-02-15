import googleapiclient.discovery
import json
import csv
from urllib.parse import urlparse, urlencode, parse_qs

from urllib.request import  urlopen

DEVELOPER_KEY = "AIzaSyCyODQsYeGLjRzbT3K5N8JEIJG6EMiWTnQ"

YOUTUBE_API_SERVICE_NAME = "youtube"

YOUTUBE_API_VERSION = "v3"

youtube = googleapiclient.dis covery.build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)





YOUTUBE_COMMENT_URL = 'https://www.googleapis.com/youtube/v3/commentThreads'

YOUTUBE_SEARCH_URL = 'https://www.googleapis.com/youtube/v3/search'

class YouTubeApi():

    def get_video_comment(self, videoid):

        def load_comments(self):

                with open("out.csv", "a") as csv_file:

                    writer = csv.writer(csv_file, delimiter=',')

                    for item in mat["items"]:

                        comment = item["snippet"]["topLevelComment"]

                        author = comment["snippet"]["authorDisplayName"]

                        text = comment["snippet"]["textDisplay"]

                        print("Comment by {}: {}".format(author, text))

                        csv_file.write(text + "\n")

                        if 'replies' in item.keys():

                            for reply in item['replies']['comments']:

                                rauthor = reply['snippet']['authorDisplayName']

                                rtext = reply["snippet"]["textDisplay"]


                            print("\n\tReply by {}: {}".format(rauthor, rtext), "\n")




                mxRes = 20

                vid = str()



        # args = parser.parse_args()





        parms = {

                    'part': 'snippet,replies',

                    'maxResults': 20,

                    'videoId': videoid,

                    'textFormat': 'plainText',

                    'key': "AIzaSyCyODQsYeGLjRzbT3K5N8JEIJG6EMiWTnQ"

                }



        try:



            matches = self.openURL(YOUTUBE_COMMENT_URL, parms)

            i = 2

            mat = json.loads(matches)

            nextPageToken = mat.get("nextPageToken")

            print("\nPage : 1")

            print("------------------------------------------------------------------")

            load_comments(self)



            while nextPageToken and i<22:

                parms.update({'pageToken': nextPageToken})

                matches = self.openURL(YOUTUBE_COMMENT_URL, parms)

                mat = json.loads(matches)

                nextPageToken = mat.get("nextPageToken")

                print("\nPage : ", i)

                print("------------------------------------------------------------------")



                load_comments(self)



                i += 1

        except KeyboardInterrupt:

            print("User Aborted the Operation")



        except:

            print("Cannot Open URL or Fetch comments at a moment")



    def openURL(self, url, parms):

              f = urlopen(url + '?' + urlencode(parms))

              data = f.read()

              f.close()

              matches = data.decode("utf-8")

              return matches
