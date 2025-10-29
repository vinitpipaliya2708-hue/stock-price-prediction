# app.py
from flask import Flask, render_template, request
import numpy as np
import yfinance as yf
import pickle
from pathlib import Path
from tensorflow.keras.models import load_model

# -----------------------------
# Config
# -----------------------------
app = Flask(__name__)
MODEL_DIR = Path(__file__).parent / "model_export"

# Load trained LSTM model
model_path = MODEL_DIR / "lstm_model.h5"
model = load_model(model_path)

# Load scaler
scaler_path = MODEL_DIR / "scaler.pkl"
with open(scaler_path, "rb") as f:
    scaler = pickle.load(f)

# -----------------------------
# Helper function to predict stock prices
# -----------------------------
def predict_stock(ticker, days):
    # Download recent stock data
    data = yf.download(ticker, period="5y")
    closing_prices = data['Close'].values.reshape(-1, 1)
    
    # Scale data
    scaled_data = scaler.transform(closing_prices)
    
    # Prepare last 60 days for prediction
    last_60 = scaled_data[-60:]
    X_input = last_60.reshape(1, 60, 1)
    
    predictions = []
    current_input = X_input.copy()
    
    for _ in range(int(days)):
        pred = model.predict(current_input, verbose=0)  # shape (1,1)
        predictions.append(pred[0][0])
        
        # reshape to 3D and slide window
        pred_reshaped = pred.reshape(1, 1, 1)
        current_input = np.concatenate((current_input[:, 1:, :], pred_reshaped), axis=1)
    
    # Inverse scale predictions
    predictions = scaler.inverse_transform(np.array(predictions).reshape(-1, 1))
    
    return predictions.flatten()

# -----------------------------
# Routes
# -----------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        ticker = request.form.get("ticker")
        days = request.form.get("days")
        try:
            days = int(days)
            predictions = predict_stock(ticker, days)
            predictions = [round(float(x), 2) for x in predictions]
            return render_template("index.html", ticker=ticker.upper(), predictions=predictions)
        except Exception as e:
            return render_template("index.html", error=str(e))
    return render_template("index.html")

# -----------------------------
# Run Flask app
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
