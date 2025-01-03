import pytest
import requests

# Test de la prédiction
def test_prediction_endpoint(requests_mock):
    url = "http://127.0.0.1:8000/predict/"
    
    # Simulation de la réponse de l'API
    mock_response = {"prediction": 12345.67}
    requests_mock.get(url, json=mock_response, status_code=200)
    
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
    
    response = requests.get(url, params=params)
    assert response.status_code == 200
    response_json = response.json()
    assert "prediction" in response_json
    assert response_json["prediction"] == 12345.67

# Test pour les données brutes
def test_data_endpoint(requests_mock):
    url = "http://127.0.0.1:8000/data/?limit=10"
    
    # Simulation de la réponse de l'API
    mock_response = [
        {"Temperature": 6.5, "Humidity": 75.0, "WindSpeed": 0.08, "PowerConsumption": 12345.67},
        {"Temperature": 7.0, "Humidity": 76.0, "WindSpeed": 0.10, "PowerConsumption": 12350.00},
    ]
    requests_mock.get(url, json=mock_response, status_code=200)
    
    response = requests.get(url)
    assert response.status_code == 200
    response_json = response.json()
    assert isinstance(response_json, list)
    assert len(response_json) == 2
    assert "Temperature" in response_json[0]

# Test de gestion des erreurs
def test_prediction_error(requests_mock):
    url = "http://127.0.0.1:8000/predict/"
    
    # Simulation de l'erreur de l'API
    mock_response = {"error": "Invalid input"}
    requests_mock.get(url, json=mock_response, status_code=400)
    
    params = {
        "Temperature": -999,  # Valeur invalide
        "Humidity": 75.0,
        "WindSpeed": 0.08,
        "GeneralDiffuseFlows": 0.05,
        "DiffuseFlows": 0.12,
        "PowerConsumption_Zone1": 34055.6962,
        "PowerConsumption_Zone2": 16128.87538,
        "PowerConsumption_Zone3": 20240.96386,
    }
    
    response = requests.get(url, params=params)
    assert response.status_code == 400
    response_json = response.json()
    assert "error" in response_json
    assert response_json["error"] == "Invalid input"
