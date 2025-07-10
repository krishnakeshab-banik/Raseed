# voice_agent.py
def respond_to_query(query_text):
    """
    Handles natural language questions.
    """
    if "detergent" in query_text.lower():
        return "Yes, you still have enough detergent for the week."
    return "Let me check your recent purchases..."
