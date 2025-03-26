import pandas as pd

# pedido = {
#       'idCliente': [2995, 3001, 1112, 9999],
#       'produto': ['Refrigerador 220V', 'Smartphone 10', 'Monitor 19 LCD', 'Mouse Logitech'],
#       'valor': [2649.99, 4999.00, 679.90, 29.90]
# }

# df = pd.DataFrame(pedido)

# print(df.loc[1])

# print(df.loc[:,["produto"]])

# df_load = pd.read_csv('data/nacionalidade-income.csv')

# print(df.info())

# print(df.describe())

df = pd.read_csv('https://www.w3schools.com/python/pandas/data.csv')

print(df.head())

df.info()

print(df.corr())

# Encontra a coluna com maior correlação com 'Duration'
correlations = df.corr()['Duration']
max_correlation = correlations.drop('Duration').idxmax()
print(f"\nColuna com maior correlação com Duration: {max_correlation}")
print(f"Valor da correlação: {correlations[max_correlation]:.4f}")

# Preenchendo valores NA com 0 apenas na coluna Duration (in place)
df['Duration'].fillna(0, inplace=True)
print("\nDataset após preencher valores NA com 0 na coluna Duration:")
print(df.head())


