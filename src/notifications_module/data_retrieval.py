import json
from datetime import datetime, timezone

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


