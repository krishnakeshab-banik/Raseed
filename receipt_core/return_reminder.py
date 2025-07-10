# return_reminder.py
from datetime import datetime, timedelta

def get_return_deadline(purchase_date, policy_days=7):
    """
    Calculates return window deadline.
    """
    date_obj = datetime.strptime(purchase_date, "%Y-%m-%d")
    return (date_obj + timedelta(days=policy_days)).strftime("%Y-%m-%d")
