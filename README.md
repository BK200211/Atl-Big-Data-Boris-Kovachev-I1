# 📊 Projet Data Lake : Analyse des Ventes de Jeux Vidéo

## 1️⃣ Introduction
Ce **Data Lake** analyse les ventes de jeux vidéo à partir de données publiques qu'on a trouvées.

## 2️⃣ Architecture du Data Lake
- **MinIO** : Pour le stockage des données
- **Jupyter Notebook & Pandas** : Pour analyser les données
- **Docker Compose** : Pour orchestrer les données

## 3️⃣ Sources de Données
- **Dataset** : vgsales.csv
- **Source** : GitHub - https://github.com/ricardocmuller/Video_Game_Sales_Analysis_and_Clustering

## 4️⃣ Technologies Utilisées
| Technologie  | À quoi ça sert |
|-------------|------|
| Docker Compose | A faire un lancement automatisé |
| MinIO | Stockage des données |
| Pandas | Manipulation des données |
| Jupyter Notebook | Exploration des données et faire des graphiques |

## 5️⃣ Implémentation
### 🔹 Pour lancer le docker
```bash
docker-compose up -d

## 6️⃣ Pipeline pour effectuer mise à jour
### 🔹 Pour lancer la mise à jour
```bash
./run_pipeline.sh
