import pandas as pd

def load_crypto_data(filepath):
    df = pd.read_csv(filepath)
    for col in df.columns:
        if 'close' in col.lower() or 'price' in col.lower():
            close_col = col
            break
    else:
        raise ValueError('Didn`t found column with close prices')
    prices = df[close_col].astype(str).str.replace(',', '').astype(float)
    return prices.dropna().reset_index(drop=True)