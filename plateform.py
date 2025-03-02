import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Charger les données
df = pd.read_csv("vgsales.csv")

# Vérifier si les données sont bien chargées
print(df.head())  # Afficher les 5 premières lignes

# Top 10 des plateformes avec le plus de ventes
top_platforms = df.groupby('Platform')['Global_Sales'].sum().sort_values(ascending=False).head(10)

# Création du graphique
plt.figure(figsize=(12,6))
sns.barplot(x=top_platforms.index, y=top_platforms.values, palette="viridis")
plt.xlabel("Plateformes")
plt.ylabel("Ventes Globales (millions)")
plt.title("Top 10 des Plateformes par Ventes Globales")
plt.xticks(rotation=45)
plt.savefig("top_platforms.png")  # Sauvegarde de l'image
plt.show()
