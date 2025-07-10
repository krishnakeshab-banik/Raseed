# scheduler.py
import datetime

def get_next_summary_schedule():
    """
    Returns next Sunday at 9am.
    """
    today = datetime.datetime.now()
    next_sunday = today + datetime.timedelta((6 - today.weekday()) % 7)
    return datetime.datetime.combine(next_sunday, datetime.time(9, 0))
