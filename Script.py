`python
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

# Verificar se 'produto_id' e 'quantidade' existem no DataFrame pedidos
if 'produto_id' in pedidos.columns and 'quantidade' in pedidos.columns:
    # Visualização de Vendas por Produto
    vendas_por_produto = pedidos.groupby('produto_id')['quantidade'].sum().reset_index()
    
    # Criar gráfico de barras
    sns.barplot(x='produto_id', y='quantidade', data=vendas_por_produto)
    plt.title('Vendas por Produto')
    plt.xlabel('Produto ID')
    plt.ylabel('Quantidade Vendida')
    plt.xticks(rotation=45)  # Rotacionar os rótulos do eixo x se necessário
    plt.show()
else:
    print("As colunas 'produto_id' ou 'quantidade' não estão presentes no DataFrame de pedidos.")
