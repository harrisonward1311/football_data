import os
from dotenv import load_dotenv

from api_module.load_functions import get_current_matchweek
from notifications_module.data_retrieval import get_current_matchweek_fixtures
from common.utils import get_absolute_path
from popup_module.popup_func import window_popup

load_dotenv()
api_key = os.getenv("FOOTBALL_DATA_API_KEY")

pl_schedule_relative_path = "output/output_pl_2026_clean.json"
pl_schedule_absolute_path = get_absolute_path(pl_schedule_relative_path)

current_pl_matchweek = get_current_matchweek("PL", api_key)

matchweek_matches = get_current_matchweek_fixtures(pl_schedule_absolute_path, current_pl_matchweek)

fixtures_text = f"Prem MW{current_pl_matchweek} Fixtures\n" + "\n".join(matchweek_matches)

window_popup(fixtures_text)

