from app import getViewCount

# validate the incoming viewCounts
def test_ViewCount():
    apiKey = 'AIzaSyAqNYjezkzxdh9IxPTbMAww0KMzH9MhQEc'
    viewCount = getViewCount(apiKey, 'schafer5')
    assert int(viewCount) > 100000