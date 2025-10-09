import pandas as pd 

# Leer el archivo JSON y cargarlo en un DataFrame
df = pd.read_json('Data/data.json')
print("Contenido del DataFrame original:")
print(df)

#filtar por la columna fecha 

df_filtrado = df[df['Fecha_nacimiento'].between('2000-01-01', '2000-12-31')]
print("Contenido del DataFrame filtrado:")
print(df_filtrado)  

