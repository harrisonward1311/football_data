import os
import tkinter as tk
from dotenv import load_dotenv

from api_module.load_functions import get_current_matchweek
from notifications_module.data_retrieval import get_current_matchweek_fixtures
from common.utils import get_absolute_path, get_league_from_args
from popup_module.popup_func import window_popup

league = get_league_from_args()

load_dotenv()
api_key = os.getenv("FOOTBALL_DATA_API_KEY")

schedule_relative_path = f"output/output_{league.lower()}_2026_clean.json"
schedule_absolute_path = get_absolute_path(schedule_relative_path)

current_matchweek = get_current_matchweek(league, api_key)

matchweek_matches = get_current_matchweek_fixtures(
	schedule_absolute_path,
	current_matchweek,
)

fixtures_text = "\n".join(matchweek_matches)

root = tk.Tk()
root.withdraw()

window_popup(
	root,
	f"{league} MW{current_matchweek} Fixtures",
	fixtures_text,
	x_position=100,
	y_position=100,
)

root.mainloop()

