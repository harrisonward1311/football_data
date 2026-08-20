import json
import uuid
from datetime import datetime
from pathlib import Path

from pyspark.sql import SparkSession
from winotify import Notification
from zoneinfo import ZoneInfo

def get_london_time_as_string(utc_date: str, utc_time: str) -> str:
    """
    Converts a UTC time string to London local time.

    Args:
        utc_date (str): The UTC date in YYYY-MM-DD format.
        utc_time (str): The UTC kickoff time in HH:MM format.

    Returns:
        str: The local time in London as a string in HH:MM format.
    """
    utc_datetime = datetime.fromisoformat(f"{utc_date}T{utc_time}:00+00:00")
    london_time = utc_datetime.astimezone(ZoneInfo("Europe/London"))

    return london_time.strftime("%H:%M")

def send_notification(title: str, message: str) -> None:
    """
    Sends a Windows notification with the given title and message.

    Args:
        title (str): The title of the notification.
        message (str): The message content of the notification.
    """
    toast = Notification(
        app_id="Football Data",
        title=title,
        msg=message,
    )
    toast.tag = uuid.uuid4().hex

    toast.show()

PROJECT_ROOT = Path(__file__).resolve().parents[2]

def create_spark_session():
    """
    Reusable function for creating a SparkSession object

    Returns:
        SparkSession object
    """ 

    return (
        SparkSession.builder
        .appName("FootballData")
        .getOrCreate()
    )

def write_results(results: list[dict], output_path: str):
    """
    Write results dictionary to storage

    Args:
        results: List of dictionaries.
        output_path: Relative path to desired output location
        
    """
    
    output_file = Path(output_path)
    if not output_file.is_absolute():
        output_file = get_absolute_path(output_path)

    output_file.parent.mkdir(parents=True, exist_ok=True)

    with output_file.open("w") as file:
        json.dump(results, file)


def get_absolute_path(relative_path: str) -> Path:
    """
    Get the absolute path of a file given its relative path.

    Args:
        relative_path (str): The relative path to the file.

    Returns:
        Path: The absolute path to the file.
    """
    return PROJECT_ROOT / relative_path