from app import getViewCount
import secrets

# validate the incoming viewCounts


def test_ViewCount(apiKey):
    
    if apiKey:
        print "Found api key from parameter"
    if not apiKey:
        apiKey = secrets.apiKey
        print "Getting api key from secrets"

    playListId = "PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS"
    viewCount = getViewCount(playListId)
    print 'viewCount: {0}'.format(viewCount)
    assert int(viewCount) != 0
