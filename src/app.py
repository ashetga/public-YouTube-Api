"""
A simple app to test the functionality of google's Youtube Data Api

We will be retreiving the following stats
   - Top 5 high viewership videos in a channel
   - Compute total duration of the entire channel
"""


from googleapiclient.discovery import build
# import secrets
import os
import re
from datetime import timedelta


def getCommaSeparatedText(iText):
    return ",".join(iText) if iText else ""


def ytAppBuilder():
    API_KEY = os.getenv('API_KEY')
    return build("youtube", "v3", developerKey=API_KEY)


def getVideosForPlaylist(iPlayListId):

    yT = ytAppBuilder()

    plRequest = yT.playlistItems().list(
        part="contentDetails", playlistId=iPlayListId)

    plResponse = plRequest.execute()
    videoIds = []

    for item in plResponse["items"]:
        videoId = item["contentDetails"]["videoId"]
        videoIds.append(videoId)
    return videoIds


def extractTimeFromDuration(iDuration, iTimePortionDesc):

    if not iDuration:
        return 0

    elif iTimePortionDesc == "HH":
        hoursPattern = re.compile(r"(\d)+H")
        rawHours = hoursPattern.search(iDuration)
        timeValue = int(rawHours.group(1)) if rawHours else 0

    elif iTimePortionDesc == "mm":
        minutesPattern = re.compile(r"(\d+)M")
        rawMinutes = minutesPattern.search(iDuration)
        timeValue = int(rawMinutes.group(1)) if rawMinutes else 0

    else:
        secondsPattern = re.compile(r"(\d+)S")
        rawSeconds = secondsPattern.search(iDuration)
        timeValue = int(rawSeconds.group(1)) if rawSeconds else 0

    return timeValue


def getTotalSecondsForVideoIds(iVideoIds):

    yT = ytAppBuilder()
    videoRequest = yT.videos().list(
        part="contentDetails", id=getCommaSeparatedText(iVideoIds)
    )

    videoResponse = videoRequest.execute()

    videoTotalSeconds = 0

    for item in videoResponse["items"]:
        duration = item["contentDetails"]["duration"]

        hours = extractTimeFromDuration(duration, "HH")
        minutes = extractTimeFromDuration(duration, "mm")
        seconds = extractTimeFromDuration(duration, "SS")

        curVideoTotalSeconds = timedelta(
            hours=hours, minutes=minutes, seconds=seconds
        ).total_seconds()

        videoTotalSeconds = videoTotalSeconds + curVideoTotalSeconds

    return videoTotalSeconds


def getViewCount(playListId):

    # let's passin a playlist
    videoList = getVideosForPlaylist(iPlayListId=playListId)
    totalSeconds = getTotalSecondsForVideoIds(iVideoIds=videoList)
    return totalSeconds


if __name__ == "__main__":
    playListId = "PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS"
    print(getViewCount(playListId))
