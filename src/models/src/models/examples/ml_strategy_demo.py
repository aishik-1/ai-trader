"""Use trained ML model to generate signals and backtest."""
import joblib
import pandas as pd
from src.models.ml_utils import build_features
from src.backtest.vectorbt_backtest import backtest_signals




def run_ml_strategy(csv_path="data/raw/ETHUSD_daily.csv"):
df = pd.read_csv(csv_path, index_col=0, parse_dates=True)
X, y = build_features(df)
model = joblib.load("data/processed/rf_model.pkl")


preds = model.predict(X)
entries = pd.Series(preds, index=df.index).astype(bool)
exits = ~entries


pf, stats = backtest_signals(df['close'], entries, exits)
print("ML strategy stats:", stats)




if __name__ == "__main__":
run_ml_strategy()
