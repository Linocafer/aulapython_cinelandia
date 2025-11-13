import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# -----------------------------
# 1. Carregar dados
# -----------------------------
try:
    df = dataset  # Power BI fornece 'dataset'
except NameError:
    df = pd.read_csv("vendas_avancadas.csv")  # Python normal
    print("Rodando fora do Power BI, CSV carregado.")

sns.set_style("whitegrid")

# -----------------------------------
# 2. Vendas por Categoria (Bar Plot)
# -----------------------------------
plt.figure(figsize=(8,5))
sns.barplot(x='Categoria', y='Vendas', data=df, palette="Blues_d")
plt.title("Vendas por Categoria", fontsize=14)
plt.xlabel("Categoria")
plt.ylabel("Vendas")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -----------------------------------
# 3. Vendas ao longo do tempo (Line Plot)
# -----------------------------------
df['Data'] = pd.to_datetime(df['Data'])
vendas_por_data = df.groupby('Data')['Vendas'].sum().reset_index()

plt.figure(figsize=(10,4))
plt.plot(vendas_por_data['Data'], vendas_por_data['Vendas'], marker='o', color='green')
plt.title("Vendas ao longo do tempo", fontsize=14)
plt.xlabel("Data")
plt.ylabel("Vendas")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -----------------------------------
# 4. Lucro vs Vendas por Região (Scatter)
# -----------------------------------
fig = px.scatter(df, x="Vendas", y="Lucro", color="Regiao", size="Quantidade",
                 title="Lucro vs Vendas por Região", size_max=30)
fig.show()

# -----------------------------------
# 5. Top 5 Produtos por Vendas
# -----------------------------------
top5_produtos = df.groupby('Produto')['Vendas'].sum().sort_values(ascending=False).head(5)
plt.figure(figsize=(6,4))
sns.barplot(x=top5_produtos.index, y=top5_produtos.values, palette="Oranges_d")
plt.title("Top 5 Produtos por Vendas", fontsize=14)
plt.xlabel("Produto")
plt.ylabel("Vendas")
plt.tight_layout()
plt.show()

# -----------------------------------
# 6. Heatmap de Correlação
# -----------------------------------
plt.figure(figsize=(6,5))
sns.heatmap(df[['Vendas','Lucro','Quantidade']].corr(), annot=True, cmap="coolwarm")
plt.title("Mapa de Correlação", fontsize=14)
plt.show()

