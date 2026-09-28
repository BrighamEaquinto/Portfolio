import requests
from pprint import pprint

def pull_tournaments():
    endpoint_tournaments = "https://fnapi.osirion.gg/v1/tournaments"

    tournaments_data = (
        requests.get(endpoint_tournaments,
            params={
                "region": "EU",
                "includeHistoricData": "false",
                "lang": "en"
                }
        )
        .json()
    )

    with open("data\\raw\\tournaments.json", "w") as f:
        f.write(str(tournaments_data))

