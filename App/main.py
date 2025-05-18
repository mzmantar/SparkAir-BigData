from pyspark.sql import SparkSession
import pandas as pd
import joblib
import numpy as np

# ───────────────────────────────────────────────────────
# 1. Initialisation de Spark
# ───────────────────────────────────────────────────────
spark = SparkSession.builder.appName("AirQualityPrediction").getOrCreate()

# ───────────────────────────────────────────────────────
# 2. Définition des features
# ───────────────────────────────────────────────────────
selected_features = [
    'PT08.S1(CO)',
    'C6H6(GT)',
    'PT08.S2(NMHC)',
    'NOx(GT)',
    'PT08.S4(NO2)',
    'T',
    'RH',
    'AH',
    'PT08.S3(NOx)'
]

# ───────────────────────────────────────────────────────
# 3. Chargement du modèle
# ───────────────────────────────────────────────────────
print("📦 Chargement du modèle...")
model = joblib.load("random_forest_model.pkl")

# ───────────────────────────────────────────────────────
# 4. Test avec des données spécifiques
# ───────────────────────────────────────────────────────
print("\n🧪 Test avec des données spécifiques :")

# Données de test
test_data = ["1360.0", "11.9", "1046.0", "166.0", "1692.0", "13.6", "48.9", "0.7578", "1056.0"]

# Création du DataFrame de test
test_data_df = pd.DataFrame([test_data], columns=selected_features)

# Conversion des données en float
for col in selected_features:
    test_data_df[col] = test_data_df[col].astype(float)

# Affichage des données de test
print("\nDonnées de test :")
for col, val in zip(selected_features, test_data):
    print(f"  {col}: {val}")

# Prédictions
print("\nPrédictions :")
predictions = model.predict(test_data_df)
print(f"  NO2: {predictions[0][0]:.3f}")
print(f"  CO:  {predictions[0][1]:.3f}")
print(f"  O3:  {predictions[0][2]:.3f}")

# ───────────────────────────────────────────────────────
# 5. Fermer Spark
# ───────────────────────────────────────────────────────
spark.stop()
