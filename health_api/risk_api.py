from flask import Flask, request, jsonify

app = Flask(__name__)

def assess_risk(glucose, haemoglobin, cholesterol):
    """Simple rule‑based health risk assessment."""
    risks = []
    
    # Glucose evaluation (mg/dL)
    if glucose < 70:
        risks.append("Hypoglycemia risk")
    elif 70 <= glucose <= 99:
        risks.append("Normal glucose")
    elif 100 <= glucose <= 125:
        risks.append("Prediabetes (impaired fasting glucose)")
    else:  # >= 126
        risks.append("Diabetes mellitus likely")
    
    # Haemoglobin evaluation (g/dL) – general ranges for adults
    if haemoglobin < 12:
        risks.append("Possible anemia (low haemoglobin)")
    elif haemoglobin > 16.5:
        risks.append("High haemoglobin (polycythemia risk)")
    else:
        risks.append("Haemoglobin normal")
    
    # Cholesterol evaluation (mg/dL)
    if cholesterol < 200:
        risks.append("Desirable cholesterol")
    elif 200 <= cholesterol < 240:
        risks.append("Borderline high cholesterol")
    else:
        risks.append("High cholesterol (cardiovascular risk)")
    
    # Combine into a final remark
    return "; ".join(risks)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    try:
        glucose = float(data['glucose'])
        haemoglobin = float(data['haemoglobin'])
        cholesterol = float(data['cholesterol'])
    except (KeyError, ValueError, TypeError):
        return jsonify({"error": "Invalid input"}), 400
    
    remarks = assess_risk(glucose, haemoglobin, cholesterol)
    return jsonify({"remarks": remarks})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)