import os
import subprocess
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def run_script(script_name, ticker):

    result = subprocess.run(
        ["python", script_name, ticker],
        cwd=BASE_DIR,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        raise Exception(result.stderr)

    return result.stdout.strip()

def pipeline(ticker):

    ticker = ticker.replace(".NS", "").upper()

    csv = os.path.join(BASE_DIR, "data", f"{ticker}.csv")
    prepared = os.path.join(BASE_DIR, "data", f"{ticker}_prepared.csv")
    model = os.path.join(BASE_DIR, "models", f"{ticker}_model.pkl")

    # Download data if missing
    if not os.path.exists(csv):
        run_script("download_data.py", ticker)

    # Prepare dataset if missing
    if not os.path.exists(prepared):
        run_script("prepare_dataset.py", ticker)

    # Train model if missing
    if not os.path.exists(model):
        run_script("train_model.py", ticker)

    prediction = run_script("predict.py", ticker)

    # ONLY print the JSON returned by predict.py
    print(prediction, end="")

if __name__ == "__main__":

    if len(sys.argv) > 1:
        ticker = sys.argv[1]
    else:
        ticker = input("Ticker: ")

    pipeline(ticker)
