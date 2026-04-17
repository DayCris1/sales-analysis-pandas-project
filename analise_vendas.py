import pandas as pd

#Leitura do arquivo CSV
df = pd.read_csv('vendas_empresa.csv', encoding = 'latin1')

#Análise dos dados
print("\n ANÁLISE")
print(df.head())
print(df.info())
print(df.describe())

#Acessando colunas específicas
print("\n PRODUTO E PREÇO")
print(df[['produto','preco']])

#Filtrando dados
print("\n FILTRO")
print(df[(df['preco'] > 100) & (df['quantidade'] > 1)])


#Filtros adicionais
print("\n FILTRO POR QUANTIDADE")
print(df[df['quantidade'] > 1])

print("\n FILTRO POR PREÇO")
print(df[df['preco'] > 100])

#Contagem de produtos vendidos
print("\n CONTAGEM DE PRODUTOS")
contagem = df['produto'].value_counts()
print(contagem)

#Identificando os 3 produtos mais vendidos
print("\n TOP 3 PRODUTOS MAIS VENDIDOS")
top3_produtos = df['produto'].value_counts().head(3).index
print(top3_produtos)

#Calculando a média de preço por categoria
print("\n MÉDIA DE PREÇO")
media_preco = df.groupby('categoria')['preco'].mean()
print(media_preco)

#Ordenando os produtos por preço
print("\n ORDEM DE PREÇO")
ordem_preco = df.sort_values(by='preco', ascending=False)
print(ordem_preco.head())

#Calculando o faturamento total por produto
print("\n FATURAMENTO POR PRODUTO")
df['total'] = df['preco'] * df['quantidade']
faturamento = df.groupby('produto')['total'].sum()
print(faturamento.sort_values(ascending=False))