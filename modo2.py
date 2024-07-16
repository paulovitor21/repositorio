import pandas as pd

# Carregar o arquivo Excel
arquivo_excel = "caminho_para_seu_arquivo.xlsx"

# Carregar a planilha como um DataFrame do pandas
df = pd.read_excel(arquivo_excel)

# Verificar as primeiras linhas do DataFrame para garantir que foi carregado corretamente
print(df.head())

# Verificar os nomes das colunas
print(df.columns)

# Supondo que a coluna que você quer verificar se chama "Resposta"
coluna = "Resposta"

# Remover espaços em branco ao redor das strings
df[coluna] = df[coluna].astype(str).str.strip()

# Converter para minúsculas para evitar problemas de maiúsculas/minúsculas
df[coluna] = df[coluna].str.lower()

# Contar quantas vezes "concordam" aparece na coluna
contagem_concordam = (df[coluna] == "concordam").sum()

print(f"Número de 'concordam' na coluna '{coluna}': {contagem_concordam}")