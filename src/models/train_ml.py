"""Train a simple ML model with MLflow logging."""
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import mlflow


from .ml_utils import build_features




def train(csv_path: str = "data/raw/ETHUSD_daily.csv"):
df = pd.read_csv(csv_path, index_col=0, parse_dates=True)
X, y = build_features(df)


X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=False, test_size=0.2)


model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
acc = model.score(X_test, y_test)


mlflow.log_metric("accuracy", acc)
joblib.dump(model, "data/processed/rf_model.pkl")
print("Model trained, accuracy:", acc)




if __name__ == "__main__":
train()
