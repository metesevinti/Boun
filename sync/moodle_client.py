import os
import requests
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

BASE_URL = os.environ["MOODLE_URL"]
TOKEN = os.environ["MOODLE_TOKEN"]
USER_ID = int(os.environ["MOODLE_USER_ID"])
API_URL = f"{BASE_URL}/webservice/rest/server.php"

COURSES = {
    85966: "ie201_programming",
    85764: "ie341_economics",
    84679: "ie423_quality",
    83575: "ie440_nonlinear",
    84273: "ie450_stochastic",
    85927: "htr311_tarih",
}


def _call(function, **params):
    params.update(wstoken=TOKEN, wsfunction=function, moodlewsrestformat="json")
    r = requests.get(API_URL, params=params)
    r.raise_for_status()
    data = r.json()
    if isinstance(data, dict) and "exception" in data:
        raise RuntimeError(f"Moodle API error: {data['message']}")
    return data


def get_user_courses():
    return _call("core_enrol_get_users_courses", userid=USER_ID)


def get_course_contents(course_id):
    return _call("core_course_get_contents", courseid=course_id)


def get_messages(unread_only=True, limit=20):
    return _call(
        "core_message_get_messages",
        useridto=USER_ID,
        type="both",
        read=0 if unread_only else 1,
        limitfrom=0,
        limitnum=limit,
    ).get("messages", [])


def get_calendar_events(limit=20):
    return _call(
        "core_calendar_get_calendar_upcoming_view",
    ).get("events", [])


def download_file(file_url, dest_path):
    url = f"{file_url}{'&' if '?' in file_url else '?'}token={TOKEN}"
    r = requests.get(url, stream=True)
    r.raise_for_status()
    dest_path = Path(dest_path)
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    with open(dest_path, "wb") as f:
        for chunk in r.iter_content(8192):
            f.write(chunk)
    return dest_path
