import os

from dotenv import load_dotenv

from common.utils import get_absolute_path, send_notification, write_results
from api_module.load_functions import fetch_2026_schedule, clean_schedule
from notifications_module.data_retrieval import get_next_liverpool_match
from notifications_module.messages import next_liverpool_pl_match_message


def main() -> None:
    load_dotenv()
    api_key = os.getenv("FOOTBALL_DATA_API_KEY")

    pl_schedule_output_path = "output/output_pl_2026_clean.json"

    pl_schedule = fetch_2026_schedule(api_key, "PL")
    pl_cleaned_schedule = clean_schedule(pl_schedule)
    write_results(pl_cleaned_schedule, pl_schedule_output_path)

    schedule_path = get_absolute_path(pl_schedule_output_path)
    next_match = get_next_liverpool_match(schedule_path)

    if next_match is None:
        print("No upcoming Liverpool fixtures found")
        return

    message = next_liverpool_pl_match_message(next_match)
    send_notification("Liverpool's Next Fixture", message)


if __name__ == "__main__":
    main()
