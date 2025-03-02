#!/bin/bash

echo "🚀 Lancement du pipeline Data Lake..."

# Étape 1 : Télécharger les données
wget -q https://raw.githubusercontent.com/ricardocmuller/Video_Game_Sales_Analysis_and_Clustering/main/vgsales.csv -O vgsales.csv
echo "📥 Données téléchargées."

# Étape 2 : Analyser les données
python3 analyze_data.py
echo "📊 Analyse terminée."

# Étape 3 : Envoyer les résultats dans MinIO
python3 upload_data.py
echo "📤 Résultats envoyés dans MinIO."

echo "✅ Pipeline terminé !"
