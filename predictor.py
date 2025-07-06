import numpy as np
from sklearn.ensemble import RandomForestRegressor

def prepare_data(series, lookback=7):
   
    X, y = [], []
    for i in range(len(series) - lookback):
        X.append(series[i:i+lookback])
        y.append(series[i+lookback])
    return np.array(X), np.array(y)

def train_and_predict(series, mode='strategist', predict_steps=7):
    lookback = 7 if mode == 'strategist' else 3
    model = RandomForestRegressor(n_estimators=120 if mode == 'risk-taker' else 60)
    X, y = prepare_data(series, lookback)
    model.fit(X, y)
    last_seq = list(series[-lookback:])
    preds = []
    for _ in range(predict_steps):
        next_pred = model.predict([last_seq])[-1]
        preds.append(next_pred)
        last_seq = last_seq[1:] + [next_pred]
    return np.array(preds)