from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import os

app = Flask(__name__)
CORS(app)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model", "model.pkl")

model = joblib.load(MODEL_PATH)


COMMANDS = ["Need Help", "Medicine", "Hungry", "Call Caregiver", "Need Water", "Yes", "No"]

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()


    command = data.get("command", None)

    if not command:
        return jsonify({"error": "No command received"}), 400

    try:
        class_idx = COMMANDS.index(command)
    except ValueError:
        return jsonify({"error": "Invalid command"}), 400

    prediction = COMMANDS[class_idx]


    print(f"✅ Predicted: {prediction}")

    return jsonify({"prediction": prediction})


if __name__ == "__main__":
    app.run(debug=True)

