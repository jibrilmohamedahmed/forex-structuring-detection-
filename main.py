from .data.loader import load_data
from .models.detector import detect_structures
from .utils.logger import get_logger

def main():
    logger = get_logger()
    logger.info("Starting Forex Structuring Detection System...")

    data = load_data()
    results = detect_structures(data)
    logger.info(f"Detection Results: {results}")

if __name__ == "__main__":
    main()