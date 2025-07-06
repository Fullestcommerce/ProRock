#  Crypto Trading Agent
**Smart ML-powered app for predicting cryptocurrency price movements and trading strategies.  

##  Features
- Loads historical crypto price data (BTC, ETH, etc) from CSV (Yahoo/Investing)
- Predicts the next 7 days of price movement using a machine learning model
- Two trading modes:
  - **Risk-Taker** — aggressive, high-reward, fast-acting signals
  - **Strategist** — conservative, stable, fewer but safer trades
- Beautiful GUI with real-time chart:
  - Historical data and prediction plotted together
  - Transparent “future” prediction line shows increasing uncertainty
- Built in Python (Tkinter, Scikit-learn, Pandas, Matplotlib)
- Easy to extend with more advanced models (LSTM, XGBoost) or more features

## Quick Start
1. Clone & install
    ```bash
    git clone https://github.com/Fullestcommerce/ProRock.git
    cd crypto-trading-agent
    pip install -r requirements.txt
2. Run the App
    bash
    Copy
    Edit
    python gui.py
3. Get historical data
    Download BTC or ETH price history from Yahoo Finance or Investing.com
    Use the Download button on the site.
    Select your .csv file in the app.
## Usage
- Click “Load CSV” and select your crypto price file.
- Choose a prediction mode: Strategist (safe) or Risk-Taker (aggressive).
- Click “Predict”.
- Wiew historical data and forecast — the orange, semi-transparent forecast line shows how uncertainty increases further into the future.
## Technologies
Python 3.8+
Tkinter (standard library GUI)
Pandas for data handling
scikit-learn for ML model (Random Forest)
matplotlib for charts
