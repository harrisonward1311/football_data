from dotenv import load_dotenv
import os

from common.utils import get_league_from_args, write_results
from api_module.load_functions import fetch_2026_schedule, clean_schedule

league = get_league_from_args()

# Load the API key from .env
load_dotenv()
api_key = os.getenv("FOOTBALL_DATA_API_KEY")

data_schedule_2026 = fetch_2026_schedule(api_key, league)
cleaned_schedule_2026 = clean_schedule(data_schedule_2026)

write_results(
	cleaned_schedule_2026,
	f"output/output_{league.lower()}_2026_clean.json",
)
