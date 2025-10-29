# LSTM Stock Price Predictor

## Project Title
LSTM Stock Price Predictor

## Description
This project is a web-based application built with Flask that leverages a Long Short-Term Memory (LSTM) neural network model to predict future stock prices. Users can input a stock ticker symbol and the number of days for which they want predictions. The application fetches historical stock data using `yfinance`, preprocesses it with a pre-trained scaler, and then uses the LSTM model to generate future price forecasts. The predictions are displayed on a simple web interface.

### Key Features:
*   **Stock Price Prediction**: Predicts future closing prices for a specified stock ticker.
*   **LSTM Model**: Utilizes a pre-trained Keras LSTM model for time-series forecasting.
*   **Data Preprocessing**: Employs a `MinMaxScaler` to normalize and denormalize stock data.
*   **Historical Data Fetching**: Integrates with `yfinance` to retrieve real-time and historical stock data.
*   **Web Interface**: Provides a user-friendly web form for input and displays predictions.

## Installation

### Prerequisites
*   Python 3.8+

### Steps
1.  **Clone the repository (if applicable):**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```
    *(Assuming the project files are in the current directory)*

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Running the Application
To start the Flask web application:

```bash
python app.py
```

The application will typically run on `http://127.0.0.1:5000`. Open this URL in your web browser.

### Web Interface
1.  **Input Stock Ticker**: Enter a valid stock ticker symbol (e.g., `AAPL`, `GOOGL`).
2.  **Input Number of Days**: Specify how many future days you want to predict (e.g., `5`).
3.  **Predict**: Click the "Predict" button to get the forecasted stock prices.

The predictions will be displayed as a list of predicted closing prices for the specified number of days.

## Project Structure

```
.
├── app.py                      # Main Flask application logic
├── requirements.txt            # Python dependencies
├── model_export/               # Directory for trained models and artifacts
│   ├── best_model.h5           # An alternative or older Keras LSTM model (not currently used by app.py)
│   ├── lstm_model.h5           # The primary Keras LSTM model used for predictions
│   ├── meta.json               # Metadata for the model (e.g., lookback period, example ticker)
│   └── scaler.pkl              # Pre-trained scikit-learn MinMaxScaler for data preprocessing
└── templates/                  # HTML templates for the web interface
    ├── index.html              # Main page with prediction form and results display
    └── result.html             # (Currently unused) Template for displaying detailed results with a chart
```

## Technologies Used

*   **Python**: Programming language
*   **Flask**: Web framework for building the application
*   **TensorFlow / Keras**: For building and loading the LSTM neural network model
*   **NumPy**: For numerical operations, especially array manipulation
*   **Pandas**: For data manipulation, particularly with `yfinance` dataframes
*   **Scikit-learn**: For data scaling (MinMaxScaler)
*   **yfinance**: Library to download historical market data from Yahoo! Finance
*   **h5py**: Python interface to the HDF5 binary data format, used by Keras for model saving/loading
*   **Bootstrap**: Frontend framework for responsive and modern UI styling
*   **Chart.js**: (Used in `result.html`) JavaScript library for creating interactive charts

## Scripts
The primary script to run the application is `app.py`.

*   **`python app.py`**: Starts the Flask development server.

## Configuration
*   **`model_export/meta.json`**: This file contains metadata such as `{"lookback": 60, "ticker": "AAPL"}`. While `app.py` currently hardcodes the `lookback` period to 60, this file serves as a record of model training parameters.
*   **`MODEL_DIR`**: Defined in `app.py`, this constant specifies the directory where model artifacts are stored.

## Contributing
Contributions are welcome! Please feel free to open issues or submit pull requests.

## License
No explicit license file was provided with the project.