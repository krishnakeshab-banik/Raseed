# whatif_agent.py
def simulate_savings(spending_data, reduction_percent):
    """
    Simulates savings if user reduces a category spend by X%.
    """
    groceries = spending_data["categories"].get("groceries", 0)
    savings = groceries * (reduction_percent / 100)
    return f"You could save ₹{savings:.2f} by reducing groceries by {reduction_percent}%"
