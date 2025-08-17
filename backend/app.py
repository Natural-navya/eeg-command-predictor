from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import os

# Flask setup
app = Flask(__name__)
CORS(app)

# Load model (adjust path if needed)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model", "model.pkl")

model = joblib.load(MODEL_PATH)

# List of commands corresponding to classes
COMMANDS = ["Need Help", "Medicine", "Hungry", "Call Caregiver", "Need Water", "Yes", "No"]

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    # In real use-case, you'd get EEG features instead of just command text
    command = data.get("command", None)

    if not command:
        return jsonify({"error": "No command received"}), 400

    # If model expects some input, you’d replace this part with preprocessing
    # For now, let's just simulate prediction
    # Example: simulate class index from button press
    try:
        class_idx = COMMANDS.index(command)
    except ValueError:
        return jsonify({"error": "Invalid command"}), 400

    # Model prediction (dummy example: just echo index)
    # Replace with: prediction = model.predict([features])[0]
    prediction = COMMANDS[class_idx]

    # Print in terminal
    print(f"✅ Predicted: {prediction}")

    return jsonify({"prediction": prediction})


if __name__ == "__main__":
    app.run(debug=True)
