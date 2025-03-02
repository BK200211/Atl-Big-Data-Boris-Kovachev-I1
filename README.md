# 📊 Projet Data Lake : Analyse des Ventes de Jeux Vidéo

## 1️⃣ Introduction
Ce **Data Lake** a pour but d'analyser les ventes de jeux vidéo à partir de données publiques.

## 2️⃣ Architecture du Data Lake
- **Stockage** : MinIO (équivalent S3)
- **Analyse des données** : Jupyter Notebook & Pandas
- **Orchestration** : Docker Compose

## 3️⃣ Sources de Données
- **Dataset** : vgsales.csv (Ventes de jeux vidéo)
- **Source** : GitHub - https://github.com/ricardocmuller/Video_Game_Sales_Analysis_and_Clustering

## 4️⃣ Technologies Utilisées
| Technologie  | Rôle |
|-------------|------|
| Docker Compose | Déploiement automatisé |
| MinIO | Stockage des données |
| Pandas | Analyse des données |
| Jupyter Notebook | Exploration des données |

## 5️⃣ Implémentation
### 🔹 Déploiement avec Docker Compose
```bash
docker-compose up -d
