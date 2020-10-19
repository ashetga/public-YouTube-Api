from app import getViewCount
import secrets
import logging

# validate the incoming viewCounts


def test_ViewCount(apiKey):
    if apiKey:
        logging.info("obtained api key from secrets")

    if not apiKey:
        apiKey = secrets.apiKey
        logging.info("reading from secrets file")

    playListId = "PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS"
    viewCount = getViewCount(playListId)
    assert int(viewCount) != 0
