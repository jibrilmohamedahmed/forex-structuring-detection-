import pandas as pd
from ..config import DATA_PATH

def load_data(path=DATA_PATH):
    """Load Forex data from a CSV file."""
    try:
        data = pd.read_csv(path)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None