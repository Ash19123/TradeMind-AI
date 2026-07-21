import os
import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def train_model(ticker):

    # Remove .NS if present
    ticker = ticker.replace(".NS", "")

    dataset_path = f"data/{ticker}_prepared.csv"

    if not os.path.exists(dataset_path):
        print(f"Prepared dataset not found: {dataset_path}")
        return False

    print(f"\nLoading dataset for {ticker}...")

    df = pd.read_csv(dataset_path)

    # Features
    X = df[
        [
            "sma20",
            "sma50",
            "ema20",
            "rsi",
            "macd",
            "bb_high",
            "bb_low",
            "daily_return",
        ]
    ]

    # Target
    y = df["target"]

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    print("Training AI model...")

    model = RandomForestClassifier(
        n_estimators=200,
        random_state=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

    os.makedirs("models", exist_ok=True)

    model_path = f"models/{ticker}_model.pkl"

    joblib.dump(model, model_path)

    print(f"Model saved to {model_path}")

    return True


if __name__ == "__main__":

    ticker = input("Enter NSE Stock Symbol: ").upper()

    train_model(ticker)
