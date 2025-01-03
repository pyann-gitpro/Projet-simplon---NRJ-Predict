import logging
import os

# Create a directory for logs if it doesn't exist
LOGS_DIR = "logs"
os.makedirs(LOGS_DIR, exist_ok=True)

# Configure the log file for Streamlit
LOG_FILE = os.path.join(LOGS_DIR, "streamlit.log")

# Configure logger for Streamlit
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, mode="a"),  # Append mode for continuous logging
        logging.StreamHandler()  # Display logs in the console
    ]
)

# Example logger specific to Streamlit
streamlit_logger = logging.getLogger("streamlit")

# Example log messages for Streamlit
if __name__ == "__main__":
    streamlit_logger.info("Streamlit app started.")
    try:
        # Simulate an operation
        streamlit_logger.debug("Loading components...")
        # Simulate success
        streamlit_logger.info("Components loaded successfully.")
    except Exception as e:
        streamlit_logger.error(f"Error in Streamlit app: {str(e)}")
