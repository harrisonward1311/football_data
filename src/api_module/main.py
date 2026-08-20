from dotenv import load_dotenv
import os

from common.utils import write_results
from api_module.load_functions import fetch_2026_schedule, clean_schedule

# Load the API key from .env
load_dotenv()
api_key = os.getenv("FOOTBALL_DATA_API_KEY")

pl_data_schedule_2026 = fetch_2026_schedule(api_key, "PL")
pl_cleaned_schedule_2026 = clean_schedule(pl_data_schedule_2026)

write_results(pl_cleaned_schedule_2026, "output/output_pl_2026_clean.json")
