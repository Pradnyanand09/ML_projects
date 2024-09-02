import logging
import os
from datetime import datetime

# Create log file with a timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y-%H-%M_%S')}.log"

# Define the directory and log file path
logs_path = os.path.join(os.getcwd(), 'logs')
os.makedirs(logs_path, exist_ok=True)  # Create the 'logs' directory if it doesn't exist

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)  # Complete log file path

# Set up basic logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="%(asctime)s - %(lineno)d - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# # Main execution
# if __name__ == "__main__":
#     logging.info("Starting")
