import yfinance as yf
import os


def download_stock(ticker):

    # Yahoo Finance requires .NS for NSE stocks
    yahoo_ticker = ticker

    # Clean name for saving files
    display_name = ticker.replace(".NS", "")

    print(f"Downloading {yahoo_ticker}...")

    data = yf.download(
        yahoo_ticker,
        period="5y",
        interval="1d",
        auto_adjust=True
    )

    # Flatten MultiIndex columns if present
    if hasattr(data.columns, "levels"):
        data.columns = data.columns.get_level_values(0)

    if data.empty:
        print("No data found.")
        return

    os.makedirs("data", exist_ok=True)

    filename = f"data/{display_name}.csv"

    data.to_csv(filename)

    print(f"Saved to {filename}")


if __name__ == "__main__":

    ticker = input("Enter NSE Stock Symbol (e.g. RELIANCE): ").upper()

    if not ticker.endswith(".NS"):
        ticker += ".NS"

    download_stock(ticker)
