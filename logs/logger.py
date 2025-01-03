import logging
import os

# Créer un dossier pour les logs s'il n'existe pas
LOGS_DIR = "logs"
os.makedirs(LOGS_DIR, exist_ok=True)

# Configurer le fichier de log pour FastAPI
LOG_FILE = os.path.join(LOGS_DIR, "fastapi.log")

# Configuration du logger pour FastAPI
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()  # Affiche les logs dans la console
    ]
)

# Exemple de logger spécifique à FastAPI
fastapi_logger = logging.getLogger("fastapi")

# Exemple de messages de log pour FastAPI
if __name__ == "__main__":
    fastapi_logger.info("FastAPI app started.")
    try:
        # Simuler une opération
        fastapi_logger.debug("Initializing routes...")
        # Simuler un succès
        fastapi_logger.info("Routes initialized successfully.")
    except Exception as e:
        fastapi_logger.error(f"Error in FastAPI app: {str(e)}")
