import pandas as pd

# Exemplo de DataFrame
data = {'col1': [1, 2, 3], 'col2': [4, 5, 6], 'col3': [7, 8, 9]}
df = pd.DataFrame(data)

# Iterar pelas colunas e seus valores
for column_name, column_data in df.iteritems():
    if column_name in ['col1', 'col2']:  # Filtrar pelas colunas desejadas
        print(column_name, column_data)