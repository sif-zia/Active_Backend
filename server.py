from flask import Flask, request, jsonify
from flask_cors import CORS
import lightgbm as lgb
import numpy as np
import joblib

app = Flask(__name__)

# Enable CORS for the app
CORS(app)

# Load the model
try:
	model = joblib.load("lgbm_model.pkl")
except Exception as e:
	print(f"Error loading the model: {e}")
	exit(1)

@app.route("/predict", methods=["POST"])
def predict():
    # input_data = request.json["data"]
    # input_array = np.array(input_data).reshape(1, -1)  # Adjust shape as necessary
    # prediction = model.predict(input_array).tolist()
    # return jsonify({"prediction": prediction})
    return "Hello World"

@app.route("/", methods=["GET"])
def home():
    return "Hello World"

if __name__ == "__main__":
    app.run(port=5000)