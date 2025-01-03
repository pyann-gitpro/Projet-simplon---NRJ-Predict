from fastapi import FastAPI
import sqlite3
import pandas as pd
import joblib
import os

# Charger le modèle de prédiction
model_path = os.path.join("..", "model", "pkl", "new_linear_model.pkl")
model = joblib.load(model_path)

# Charger le scaler our la normalisation
scaler_path = os.path.join("..", "model", "pkl", "mmScaler.pkl")
scaler = joblib.load(scaler_path)

# Créer une instance de FastAPI
app = FastAPI()

# Chemin vers la base de données SQLite
DB_PATH = "../data/power_consumption.db"

#ENDPOINTS CREES
# quelques endpoints classique
#
# Endpoint root
@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API de prédiction de consommation électrique"}

# Endpoint pour récupérer des données depuis SQLite (10 premiers)
@app.get("/data/")
def get_data(limit: int = 5):
    conn = sqlite3.connect(DB_PATH)
    query = f"SELECT * FROM power_consumption LIMIT {limit}"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df.to_dict(orient="records")

# Endpoint pour effectuer une prédiction
@app.get("/predict/")
def predict(
    Temperature: float,
    Humidity: float,
    WindSpeed: float,
    GeneralDiffuseFlows: float,
    DiffuseFlows: float,
    PowerConsumption_Zone1: float,
    PowerConsumption_Zone2: float,
    PowerConsumption_Zone3: float 
):
    columns = [
    "Temperature", "Humidity", "WindSpeed",
    "GeneralDiffuseFlows", "DiffuseFlows",
    "PowerConsumption_Zone1", "PowerConsumption_Zone2", "PowerConsumption_Zone3"
    ]
    
    input_data = [[
        Temperature,
        Humidity,
        WindSpeed,
        GeneralDiffuseFlows,
        DiffuseFlows,
        PowerConsumption_Zone1,
        PowerConsumption_Zone2,
        PowerConsumption_Zone3
    ]]
    print(f"Input data: {input_data}")
    
    try:
        input_data_df = pd.DataFrame(input_data, columns=columns)
        data_normalized = scaler.transform(input_data_df)
        print(f"Normalized data: {data_normalized}")
        prediction = model.predict(data_normalized)
        print(f"Prediction: {prediction}")
        return {"prediction": prediction[0]}
    except ValueError as e:
        print(f"Erreur : {e}")
        return {"error": f"Erreur lors de la prédiction : {e}"}


