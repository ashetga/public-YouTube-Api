"""
A simple app to test the functionality of google's Youtube Data Api

We will be retreiving the following stats
   - Top 5 high viewership videos in a channel
   - Compute total duration of the entire channel
"""


from googleapiclient.discovery import build
import secrets


def getViewCount(apiKey, userName):

    # build a service
    yT = build("youtube", "v3", developerKey=apiKey)

    # generate Stats request for a given channel
    request = yT.channels().list(part="statistics", forUsername=userName)

    # collect stats
    response = request.execute()

    # extract viewCount
    viewCount = response["items"][0]["statistics"]["viewCount"]
    return viewCount


if __name__ == "__main__":
    apiKey = secrets.apiKey
    viewCount = getViewCount(apiKey, secrets.userName)

    print(viewCount)
