from flask import Flask, request, jsonify
import joblib
import numpy as np
import os

app = Flask(__name__)
# recuparation des chemin d'accès
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#construction des chemin vers les modèles
model_path = os.path.join(BASE_DIR, 'modele_XGBoost_abandon.pkl')
scaler_path = os.path.join(BASE_DIR, 'mon_scaler.pkl')
# Chargement du modèle et du scaler

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    # On tranforme les données reçues en tableau numpy
    features = np.array(data['features']).reshape(1, -1)
    # scaling
    features_scaled = scaler.transform(features)
    #Prediction
    resultat_pred= model.predict(features_scaled)
    proba_pred = float (model.predict_proba(features_scaled)[0] [1])
    return jsonify ({
        'abandon': int(resultat_pred[0]),
        'probabilité' : proba_pred
    })
if __name__=='__main__':
    app.run(port=5000, debug=True)

