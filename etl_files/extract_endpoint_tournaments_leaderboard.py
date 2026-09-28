import requests
from pprint import pprint

def pull_tournaments_leaderboard(leaderboardEventId, leaderboardEventWindowId) -> None:

    endpoint_tournaments_leaderboard = "https://fnapi.osirion.gg/v1/tournaments/leaderboard"

    tournaments_leaderboard_data = (
        requests.get(
            endpoint_tournaments_leaderboard,
            params={
                "leaderboardEventId": leaderboardEventId,
                "leaderboardEventWindowId": leaderboardEventWindowId,
                "page": "0"
            }
        )
        .json()
    )

    with open("data\\raw\\tournaments_leaderboard.json", "w") as f:
        f.write(str(tournaments_leaderboard_data))

