
# PROJET PREDICT ENERGETIQUE AU MARROCO

Bienvenue dans ce projet de prédiction de la consommation énergétique au Maroc. Ce projet utilise des techniques de machine learning pour estimer la consommation d'énergie, en se basant sur des données historiques.

## Fonctionnalités 🌟
- Prédiction de la consommation énergétique basée sur des données historiques.
- Interface utilisateur interactive pour visualiser les résultats.
- API RESTful pour accéder aux données et aux prédictions.

**Langage** : Python 3.9
Les bibliothèques suivantes doivent être installées :

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![MySQL](https://img.shields.io/badge/mysql-4479A1.svg?style=for-the-badge&logo=mysql&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-%23ffffff.svg?style=for-the-badge&logo=Streamlit&logoColor=black)


## Installation 🔧
1. Clonez le dépôt:
   ```bash
   git clone https://github.com/CARDONAJOSE/nom_du_projet.git
   cd nom_du_projet
   ```

2. Installez les dépendances:
   ```bash
   pip install -r requirements.txt
   ```

3. Lancez l'API FastAPI:
   ```bash
   uvicorn main:app --reload
   ```

4. Lancez l'application Streamlit:
   ```bash
   streamlit run app.py
   ```

## Structure des fichiers

Voici l'arborescence du projet :

```bash
├── .venv/
├── Api/
│   └── main.py
|
├── Data/
│   ├── processed/
│   ├── new_power_consumption.csv
│   ├── pro-datatest.csv
|   ├── raw/
│   ├── datsets.csv
|   ├── power_consumption.csv
│   └── power_conumption.db
|
├── model/
│   ├── mmscaler.pkl
│   └── new_linear_model.pkl
|
├── notebook/
│   ├── data-processing.ipynb
│   └── fastAPI&Lit.ipynb
|
├── public/
│   ├── asset/
│   ├── archi1.png
│   ├── archi2.png
│   └── png_consumption.png
|
├── .gitignore
├── readme.md
├── requirements.txt
```
## Auteurs
- Jose Cardona
[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jose-fabian-cardona-hernandez/)

- Yann Paaeho
[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/yann-paaeho/)

- Jule ndiaye
[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jules-ndiaye-53b52b170/)

- Ahmed 
[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jose-fabian-cardona-hernandez/)