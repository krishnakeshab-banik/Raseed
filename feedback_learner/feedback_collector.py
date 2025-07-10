# feedback_collector.py
def store_feedback(user_id, feedback_type, message):
    """
    Stores thumbs-up/down or emoji reactions.
    """
    return {"user": user_id, "feedback": feedback_type, "message": message}
