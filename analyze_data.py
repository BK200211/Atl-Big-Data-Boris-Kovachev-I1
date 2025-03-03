import pandas as pd

df = pd.read_csv("vgsales.csv")

print(df.head())

top_games = df[['Name', 'Global_Sales']].sort_values(by='Global_Sales', ascending=False).head()
print("\n🎮 Top 5 jeux les plus vendus :")
print(top_games)
