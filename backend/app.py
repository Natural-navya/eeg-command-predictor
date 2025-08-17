from flask import Flask, request, jsonify
import os
import joblib
import numpy as np
import pyttsx3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allow cross-origin requests from frontend

# Load the EEG model
BASE_DIR = os.getcwd()  # safer in VS Code terminal
model_path = os.path.join(BASE_DIR, 'model', 'model.pkl')
model = joblib.load(model_path)
print("Model loaded successfully!")

# Initialize text-to-speech engine
engine = pyttsx3.init()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    if 'eeg_signal' not in data:
        return jsonify({"error": "No EEG signal provided"}), 400
    
    eeg_signal = np.array(data['eeg_signal']).reshape(1, -1)  # reshape for model
    
    # Predict command
    prediction = model.predict(eeg_signal)
    command = str(prediction[0])  # convert to string if needed
    
    # Speak the command
    engine.say(command)
    engine.runAndWait()
    
    # Return JSON response
    return jsonify({"command": command})

if __name__ == "__main__":
    app.run(debug=True)


