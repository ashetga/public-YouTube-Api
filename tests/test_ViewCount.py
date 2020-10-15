from app import getViewCount
import secrets

# validate the incoming viewCounts


def test_ViewCount():
    apiKey = secrets.apiKey
    viewCount = getViewCount(apiKey, secrets.userName)
    assert int(viewCount) > 100000
