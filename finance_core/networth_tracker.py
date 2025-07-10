# networth_tracker.py
def calculate_net_worth(assets, liabilities):
    """
    Computes net worth.
    """
    return sum(assets.values()) - sum(liabilities.values())
