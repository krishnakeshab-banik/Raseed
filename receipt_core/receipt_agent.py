# receipt_agent.py
from firebase_admin import firestore

def parse_receipt(image_or_text):
    """
    Parses receipt from image or text using OCR and stores structured data.
    """
    # Placeholder: Use Gemini Vision / OCR model here
    parsed_data = {
        "vendor": "ABC Store",
        "date": "2025-07-10",
        "total": 123.45,
        "items": [
            {"name": "Milk", "price": 45},
            {"name": "Bread", "price": 78.45}
        ]
    }
    return parsed_data
