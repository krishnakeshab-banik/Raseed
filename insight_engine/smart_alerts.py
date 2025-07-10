# smart_alerts.py
def generate_alerts(summary):
    """
    Returns alerts based on thresholds (e.g., overspending).
    """
    alerts = []
    if summary["total"] > 10000:
        alerts.append("⚠️ You’ve crossed ₹10,000 in total spending.")
    return alerts
