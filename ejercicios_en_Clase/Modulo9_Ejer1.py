import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo CSV
data = pd.read_csv('Data/datos_groupby.csv', sep=',', encoding='utf-8')
print(data.head())

print(data.columns) 

data.columns = data.columns.str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')
data.columns = data.columns.str.strip()
print(data.columns)

# Agrupar los datos por la columna 'Categoria' y calcular la suma de 'Valor'
grouped_data = data.groupby('Categoria')['Cantidad Vendida'].sum().reset_index()  
print(grouped_data)

# Crear un gráfico de barras para visualizar los datos agrupados
plt.bar(grouped_data['Categoria'], grouped_data['Cantidad Vendida'], color='skyblue')
plt.xlabel('Categoría')
plt.ylabel('Suma de Valores')
plt.title('Suma de Valores por Categoría')
plt.show()