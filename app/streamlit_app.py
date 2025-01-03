import streamlit as st
import requests

# Configuration de l'application
st.title("Prédiction de Consommation Électrique - Tétouan - MAROC")
st.write("Cette application utilise un modèle de machine learning pour prédire la consommation électrique moyenne de la ville.")

# Entrée utilisateur pour les prédictions
Temperature = st.number_input("Température", value=6.5)
Humidity = st.number_input("Humidité (%)", value=75.0)
WindSpeed = st.number_input("Vitesse du vent", value=0.08)
GeneralDiffuseFlows = st.number_input("Débit fluide souterrain general", value=0.05)
DiffuseFlows = st.number_input("Débit fluide", value=0.12)
PowerConsumption_Zone1 = st.number_input("Conso Zone 1", value=34055.6962)
PowerConsumption_Zone2 = st.number_input("Conso Zone 2", value=16128.87538)
PowerConsumption_Zone3 = st.number_input("Conso Zone 3", value=20240.96386)

if st.button("Prédire"):
    response = requests.get(
        "http://127.0.0.1:8000/predict/",
        params={
            "Temperature": Temperature,
            "Humidity": Humidity,
            "WindSpeed": WindSpeed,
            "GeneralDiffuseFlows": GeneralDiffuseFlows,
            "DiffuseFlows": DiffuseFlows,
            "PowerConsumption_Zone1": PowerConsumption_Zone1,
            "PowerConsumption_Zone2": PowerConsumption_Zone2,
            "PowerConsumption_Zone3": PowerConsumption_Zone3,
        },
    )
    if response.status_code == 200:
        response_json = response.json()
        if "prediction" in response_json:
            prediction = response_json["prediction"]
            st.success(f"La consommation prévue est de : {prediction:.2f}")
        elif "error" in response_json:
            st.error(f"Erreur : {response_json['error']}")
        else:
            st.error("Réponse inattendue de l'API.")
    else:
        st.error(f"Erreur lors de l'appel à l'API : {response.status_code}")


# Affichage des données brutes
st.write("### Données disponibles")
limit = st.slider("Nombre de lignes à afficher", min_value=1, max_value=50, value=10)
data_response = requests.get(f"http://127.0.0.1:8000/data/?limit={limit}")
if data_response.status_code == 200:
    st.write(data_response.json())
else:
    st.error("Erreur lors de la récupération des données")
