from flask import Flask, request, jsonify
from flask_cors import CORS
import lightgbm as lgb
import numpy as np

app = Flask(__name__)

# Enable CORS for the app
CORS(app)

# Load the model
# model = lgb.Booster(model_file="lightgbm_model.txt")

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