# insight_agent.py
def analyze_spending(receipts):
    """
    Aggregates receipts to identify total spend and categories.
    """
    summary = {"total": 0, "categories": {}}
    for r in receipts:
        summary["total"] += r["total"]
        for item in r["items"]:
            category = item.get("category", "uncategorized")
            summary["categories"].setdefault(category, 0)
            summary["categories"][category] += item["price"]
    return summary
