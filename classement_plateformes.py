import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("vgsales.csv")

print(df.head())

top_platforms = df.groupby('Platform')['Global_Sales'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12,6))
sns.barplot(x=top_platforms.index, y=top_platforms.values, palette="viridis")
plt.xlabel("Plateformes")
plt.ylabel("Ventes Globales (millions)")
plt.title("Top 10 des Plateformes par Ventes Globales")
plt.xticks(rotation=45)
plt.savefig("top_platforms.png")
plt.show()
