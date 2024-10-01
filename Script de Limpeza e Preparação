import pandas as pd

# Carregar dados brutos
pedidos = pd.read_csv('data/raw_pedidos.csv')

# Remover duplicatas
pedidos = pedidos.drop_duplicates()

# Tratar valores faltantes
pedidos['status_pedido'].fillna('Indefinido', inplace=True)

# Salvar dados processados
pedidos.to_csv('data/clean_pedidos.csv', index=False)
