import json
from datetime import datetime


LOG_FILE = "route_log.jsonl"


def log_request(message, intent_data, response):

    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "message": message,
        "intent": intent_data.get("intent"),
        "confidence": intent_data.get("confidence"),
        "response": response
    }

    try:
        with open(LOG_FILE, "a") as file:
            file.write(json.dumps(log_entry) + "\n")

    except Exception as e:
        print("Logging error:", e)