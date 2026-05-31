'''
import requests
from django.conf import settings

HEALTH_API_URL = getattr(settings, 'HEALTH_API_URL', 'http://127.0.0.1:5001/predict')


def generate_remark(glucose, haemoglobin, cholesterol):
    """
    Generate a health risk assessment based on blood test results.
    
    Args:
        glucose: Glucose level (mg/dL)
        haemoglobin: Haemoglobin level (g/dL)
        cholesterol: Cholesterol level (mg/dL)
    
    Returns:
        str: Health risk assessment or error message
    """
    try:
        response = requests.post(
            HEALTH_API_URL,
            json={
                'glucose': glucose,
                'haemoglobin': haemoglobin,
                'cholesterol': cholesterol
            },
            timeout=5
        )
        if response.status_code == 200:
            return response.json().get('remarks', 'No prediction available')
        else:
            return f"API error: {response.status_code}"
    except Exception as e:
        return f"Prediction service unavailable: {e}"
'''

import os
import requests

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")  

GEMINI_URL = (
    "https://generativelanguage.googleapis.com/v1beta/models/"  
    "gemini-2.5-flash:generateContent"                          
)

def generate_remark(glucose, haemoglobin, cholesterol):
    prompt = (
        f"Blood test results:\n"
        f"Glucose: {glucose} mg/dL\n"
        f"Haemoglobin: {haemoglobin} g/dL\n"
        f"Cholesterol: {cholesterol} mg/dL\n\n"
        "Predict the most likely health condition or disease risk.\n"
        "Return ONLY one of the following labels:\n"
        "- Normal\n"
        "- Pre-Diabetic Risk\n"
        "- Diabetic Risk\n"
        "- Anemia Risk\n"
        "- High Cholesterol Risk\n"
        "- Multiple Risk Factors\n\n"
        "If multiple risk factors are present, state the factors and the risk level (Low, Moderate, High)."
        "if not normal, state the factors and the risk level (Low, Moderate, High)"
    )
    
    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }

    try:
        response = requests.post(
            GEMINI_URL,
            params={"key": GEMINI_API_KEY},
            json=payload,
            timeout=15
        )

        if response.status_code == 200:
            data = response.json()
            candidates = data.get("candidates", [])
            if candidates and "content" in candidates[0]:
                parts = candidates[0]["content"].get("parts", [])
                if parts:
                    return parts[0]["text"].strip()
            return "AI returned no prediction."

        elif response.status_code == 400:
            return "Bad request – check the prompt or API key."
        elif response.status_code == 403:
            return "API key invalid or expired."
        elif response.status_code == 404:
            return "Model not found – check model name and API version."
        elif response.status_code == 429:
            return "Rate limit exceeded. Wait a minute and try again."
        else:
            return f"Gemini API error (HTTP {response.status_code})"

    except requests.exceptions.Timeout:
        return "Gemini API timed out."
    except requests.exceptions.RequestException:
        return "Network error – cannot reach Gemini API."
    
