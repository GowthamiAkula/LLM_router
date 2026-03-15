import os
import requests
from dotenv import load_dotenv

load_dotenv()

HF_API_KEY = os.getenv("HF_API_KEY")

API_URL = "https://router.huggingface.co/hf-inference/models/facebook/bart-large-mnli"

headers = {
    "Authorization": f"Bearer {HF_API_KEY}"
}


def classify_intent(message: str):

    labels = ["code", "data", "writing", "career"]

    payload = {
        "inputs": message,
        "parameters": {"candidate_labels": labels}
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        result = response.json()

        print("HF RESPONSE", result)

        if isinstance(result, list) and len(result) > 0:

            intent = result[0]["label"]
            confidence = float(result[0]["score"])

            # confidence threshold
            if confidence < 0.30:
                return {"intent": "unclear", "confidence": confidence}

            return {"intent": intent, "confidence": confidence}

        return {"intent": "unclear", "confidence": 0.0}

    except Exception as e:
        print("Classifier error:", e)
        return {"intent": "unclear", "confidence": 0.0}