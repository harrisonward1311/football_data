import json
from datetime import datetime, timezone
from common.utils import get_london_time_as_string

def get_next_liverpool_match(file_path: str) -> dict | None:
    """
    Reads a cleaned fixture schedule from a JSON file 
    and filters for next Liverpool match.

    Args:
        file_path (str): The path to the JSON file containing the cleaned schedule.
    """
    with open(file_path) as file:
        matches = json.load(file)

    today = datetime.now(timezone.utc).date().isoformat()
    liverpool_matches = [
        match for match in matches
        if "LIV" in (match["homeTeam_tla"], match["awayTeam_tla"])
        and match["date"] >= today
    ]

    if not liverpool_matches:
        return None

    return min(liverpool_matches, key=lambda match: match["date"])

def get_current_matchweek_fixtures(file_path: str, current_matchweek: int) -> list[str]:
    """
    Reads a cleaned fixture schedule from a JSON file 
    and filters for fixtures in the current matchweek.

    Args:
        file_path (str): The path to the JSON file containing the cleaned schedule.
        current_matchweek (int): The current matchweek number.
    """
    with open(file_path) as file:
        matches = json.load(file)
    
    current_matchweek_matches = sorted(
        (
            match for match in matches
            if match["matchday"] == current_matchweek
        ),
        key=lambda match: (match["date"], match["kickoff_time_utc"]),
    )

    matches_list = []

    for match in current_matchweek_matches:
        home_team = match["homeTeam_tla"]
        away_team = match["awayTeam_tla"]
        match_date = datetime.strptime(match["date"], "%Y-%m-%d")
        day = match_date.strftime("%a")
        kickoff_time = get_london_time_as_string(
                match["date"],
                match["kickoff_time_utc"],
            )

        matches_list.append(
            f"""{home_team} vs {away_team} - {day} at {kickoff_time}"""
        )

    return matches_list
