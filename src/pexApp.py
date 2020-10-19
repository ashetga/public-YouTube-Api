import requests
from pprint import pprint
import secrets


def getTakeDownPct(authToken, header, url):
    assets = requests.get(url=url, headers=header).json()

    takeDowns = 0
    totalAssets = len(assets)

    for asset in assets:
        takeDowns += 1 if asset["is_taken_down"] else takeDowns

    return takeDowns // totalAssets


def run():
    authToken = secrets.authToken
    header = {"Authorization": f"Bearer {authToken}"}
    url = secrets.url

    pprint(getTakeDownPct(authToken, header, url))


if __name__ == "__main__":
    run()
