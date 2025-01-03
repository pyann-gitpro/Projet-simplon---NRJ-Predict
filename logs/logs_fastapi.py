import logging
import os

# Create a directory for logs if it doesn't exist
LOGS_DIR = "logs"
os.makedirs(LOGS_DIR, exist_ok=True)

# Configure the log file for FastAPI
LOG_FILE = os.path.join(LOGS_DIR, "fastapi.log")

# Configure logger for FastAPI
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, mode="a"),  # Append mode for continuous logging
        logging.StreamHandler()  # Display logs in the console
    ]
)

# Example logger specific to FastAPI
fastapi_logger = logging.getLogger("fastapi")

# Example log messages for FastAPI
if __name__ == "__main__":
    fastapi_logger.info("FastAPI app started.")
    try:
        # Simulate an operation
        fastapi_logger.debug("Initializing routes...")
        # Simulate success
        fastapi_logger.info("Routes initialized successfully.")
    except Exception as e:
        fastapi_logger.error(f"Error in FastAPI app: {str(e)}")
