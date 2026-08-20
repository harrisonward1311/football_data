import os
import tkinter as tk

from dotenv import load_dotenv

from common.utils import (
    get_absolute_path,
    get_league_from_args,
    send_notification,
    write_results,
)
from api_module.load_functions import fetch_2026_schedule, clean_schedule
from api_module.load_functions import get_current_matchweek
from notifications_module.data_retrieval import (
    get_current_matchweek_fixtures,
    get_next_liverpool_match,
)
from notifications_module.messages import next_liverpool_pl_match_message
from popup_module.popup_func import window_popup


def main() -> None:
    league = get_league_from_args()
    load_dotenv()
    api_key = os.getenv("FOOTBALL_DATA_API_KEY")

    schedule_output_path = f"output/output_{league.lower()}_2026_clean.json"

    schedule = fetch_2026_schedule(api_key, league)
    cleaned_schedule = clean_schedule(schedule)
    write_results(cleaned_schedule, schedule_output_path)

    schedule_path = get_absolute_path(schedule_output_path)

    if league in ("PL", "CL"):
        next_match = get_next_liverpool_match(schedule_path)

        if next_match is not None:
            message = next_liverpool_pl_match_message(next_match)
            send_notification("Liverpool's Next Fixture", message)
        else:
            send_notification("", "No upcoming Liverpool fixtures found")

    current_matchweek = get_current_matchweek(league, api_key)
    matchweek_matches = get_current_matchweek_fixtures(
        schedule_path,
        current_matchweek,
    )

    root = tk.Tk()
    root.withdraw()

    window_popup(
        root,
        f"{league} MW{current_matchweek} Fixtures",
        "\n".join(matchweek_matches),
        x_position=100,
        y_position=100,
    )

    root.mainloop()


if __name__ == "__main__":
    main()
