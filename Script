import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar dados
clientes = pd.read_csv('data/clientes.csv')
pedidos = pd.read_csv('data/pedidos.csv')
produtos = pd.read_csv('data/produtos.csv')
feedbacks = pd.read_csv('data/feedbacks.csv')

# Análise Exploratória
print(clientes.info())
print(pedidos.describe())

# Visualização de Vendas por Produto
vendas_por_produto = pedidos.groupby('produto_id')['quantidade'].sum()
sns.barplot(x=vendas_por_produto.index, y=vendas_por_produto.values)
plt.title('Vendas por Produto')
plt.show()
