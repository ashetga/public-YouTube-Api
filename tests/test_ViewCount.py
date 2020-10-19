from app import getViewCount
import secrets

# validate the incoming viewCounts


def test_ViewCount(apiKey):
    if not apiKey:
        apiKey = secrets.apiKey

    playListId = "PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS"
    viewCount = getViewCount(playListId)
    assert int(viewCount) != 0
