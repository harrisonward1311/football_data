import requests
from datetime import datetime

def fetch_2026_schedule(api_key: str, competition: str):

    """
    Fetches the 2026 schedule from the football-data.org API.
    
    Args:
        api_key (str): The API key for authentication.
        competition (str): The competition for which to fetch the schedule.

    Returns:
        data: The JSON data containing the schedule information.
    """

    url = f"https://api.football-data.org/v4/competitions/{competition}/matches?season=2026"
    headers = {"X-Auth-Token": api_key}

    response = requests.get(url, headers=headers)
    response.raise_for_status()  # raises an error if the request failed

    data = response.json()

    return data

def clean_schedule(data: dict):

    """
    Cleans the schedule data by extracting relevant fields.
    
    Args:
        data (dict): The raw JSON data containing the schedule information.
    
    Returns:
        list[dict]: The cleaned schedule data.
    """

    clean_matches = [
        {
            "date": datetime.fromisoformat(
                match["utcDate"].replace("Z", "+00:00")
            ).date().isoformat(),
            "kickoff_time_utc": datetime.fromisoformat(
                match["utcDate"].replace("Z", "+00:00")
            ).time().isoformat(timespec="minutes"),
            "matchday": match["matchday"],
            "homeTeam_tla": match["homeTeam"]["tla"],
            "awayTeam_tla": match["awayTeam"]["tla"],
            "homeTeam_shortname": match["homeTeam"]["shortName"],
            "awayTeam_shortname": match["awayTeam"]["shortName"],
        }
        for match in data["matches"]
    ]

    return clean_matches    