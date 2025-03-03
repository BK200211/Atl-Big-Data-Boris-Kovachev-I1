import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("vgsales.csv")

print(df.head())

top_genres = df.groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(12,6))
sns.barplot(x=top_genres.index, y=top_genres.values, palette="coolwarm")
plt.xlabel("Genres de Jeux")
plt.ylabel("Ventes Globales (millions)")
plt.title("Ventes Globales par Genre de Jeu Vidéo")
plt.xticks(rotation=45)
plt.savefig("top_genres.png")
plt.show()
