from datetime import datetime
from common.utils import get_london_time_as_string

def next_liverpool_pl_match_message(next_pl_match: dict) -> str:
    """
    Generates a message string for the next Liverpool match.

    Args:
        next_match (dict): A dictionary containing details of the next Liverpool match.
    """

    match_date = datetime.strptime(next_pl_match["date"], "%Y-%m-%d")

    if next_pl_match["homeTeam_tla"] == "LIV":
        opponent = next_pl_match["awayTeam_shortname"]
        location = "at home"
    else:
        opponent = next_pl_match["homeTeam_shortname"]
        location = "away"

    local_time = get_london_time_as_string(
        next_pl_match["date"],
        next_pl_match["kickoff_time_utc"],
    )

    message = (
        f"""Liverpool's next PL match is {location} against {opponent}\n"""
        f"""{match_date.strftime("%A %d %B")} at {local_time}"""
    )

    return message
