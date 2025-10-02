import os
import yfinance as yf

def fetch_nvda_to_csv(start="2025-05-08", end="2025-07-04", filename=None):
    data = yf.download("ETERNAL.NS", start=start, end=end, interval='15m')
    if filename is None:
        filename = f"SBIN_{start}to{end}.csv"
    data.to_csv(filename)
    full_path = os.path.abspath(filename)
    print(f"Saved CSV to: {full_path}")
    return full_path

if _name_ == "_main_":
    fetch_nvda_to_csv()