from dotenv import load_dotenv
import os

from common.utils import write_results
from api_functions import fetch_2026_schedule, clean_2026_schedule

# Load the API key from .env
load_dotenv()
api_key = os.getenv("FOOTBALL_DATA_API_KEY")

data_schedule_2026 = fetch_2026_schedule(api_key)

cleaned_schedule_2026 = clean_2026_schedule(data_schedule_2026)

write_results(cleaned_schedule_2026, "output/output_pl_2026_clean.json")
