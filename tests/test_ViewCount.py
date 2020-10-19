from app import getViewCount
import secrets

# validate the incoming viewCounts


def test_ViewCount(apiKey):
    if apiKey:
        print('Found api key from parameter')
    if not apiKey:
        apiKey = secrets.apiKey
        print('Getting api key from secrets')
    print(f'Matches? {apiKey == "AIzaSyBlk9y7rqdQEhuEpaZJR5JYgZTtUaziAg4"}')

    playListId = "PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS"
    viewCount = getViewCount(playListId)
    print(f'viewCount: {viewCount}')
    assert int(viewCount) == 10
