from app import getViewCount
import test_secrets

# validate the incoming viewCounts
def test_ViewCount():
    apiKey = test_secrets.apiKey
    viewCount = getViewCount(apiKey, test_secrets.userName)
    assert int(viewCount) > 100000