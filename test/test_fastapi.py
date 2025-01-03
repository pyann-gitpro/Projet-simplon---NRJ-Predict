import pytest
from fastapi.testclient import TestClient
from api.main import app  # Remplacez `your_api_filename` par le nom de votre fichier FastAPI
import sqlite3

client = TestClient(app)

# Test de l'endpoint racine
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenue sur l'API de prédiction de consommation électrique"}

# Test de l'endpoint pour récupérer des données
def test_get_data():
    response = client.get("/data/?limit=5")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) <= 5  # Vérifie que le nombre de lignes est conforme à la limite demandée
    if data:  # Si des données existent, vérifie les clés attendues
        assert "Temperature" in data[0]

# Test de l'endpoint de prédiction avec des données valides
def test_predict_valid():
    params = {
        "Temperature": 6.5,
        "Humidity": 75.0,
        "WindSpeed": 0.08,
        "GeneralDiffuseFlows": 0.05,
        "DiffuseFlows": 0.12,
        "PowerConsumption_Zone1": 34055.6962,
        "PowerConsumption_Zone2": 16128.87538,
        "PowerConsumption_Zone3": 20240.96386,
    }
    response = client.get("/predict/", params=params)
    assert response.status_code == 200
    data = response.json()
    assert "prediction" in data
    assert isinstance(data["prediction"], (float, int))  # Vérifie que la prédiction est un nombre

# Test de l'endpoint de prédiction avec des données invalides
def test_predict_invalid():
    params = {
        "Temperature": "invalid",  # Température invalide
        "Humidity": 75.0,
        "WindSpeed": 0.08,
        "GeneralDiffuseFlows": 0.05,
        "DiffuseFlows": 0.12,
        "PowerConsumption_Zone1": 34055.6962,
        "PowerConsumption_Zone2": 16128.87538,
        "PowerConsumption_Zone3": 20240.96386,
    }
    response = client.get("/predict/", params=params)
    assert response.status_code == 422  # Vérifie que l'API retourne une erreur de validation

# Test de gestion des erreurs lorsque la base de données est inaccessible
def test_get_data_db_error(monkeypatch):
    def mock_connect(*args, **kwargs):
        raise sqlite3.OperationalError("Database unavailable")

    monkeypatch.setattr("sqlite3.connect", mock_connect)
    response = client.get("/data/?limit=5")
    assert response.status_code == 500  # Code d'erreur pour une défaillance interne
    assert "error" in response.json()
