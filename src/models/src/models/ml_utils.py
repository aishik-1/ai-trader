import pandas as pd
import numpy as np
from src.features.indicators import sma, rsi




def build_features(df: pd.DataFrame):
close = df['close']
df_feat = pd.DataFrame(index=df.index)
df_feat['sma_fast'] = sma(close, 10)
df_feat['sma_slow'] = sma(close, 50)
df_feat['rsi'] = rsi(close)
df_feat = df_feat.fillna(0)


# Label: next-day return > 0 => 1 else 0
df_feat['target'] = (close.shift(-1) > close).astype(int)
y = df_feat['target']
X = df_feat.drop(columns=['target'])
return X, y
