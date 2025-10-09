import pandas as pd

#leer archivo json 
df=pd.read_json("data/personas.json")
#imprimir el dataframe
print(df)
#normalizar el json
f_normalizado = pd.json_normalize(df['Estudios'])
#df_normalizado = pd.concat([df.drop(columns="Estudios")])
print(f_normalizado)

df_final = pd.concat([df.drop(columns="Estudios"), f_normalizado], axis=1)
print(df_final)

#exportar a excel
df_final.to_excel('Data/personasJson.xlsx', index=False)
print('Se creo el archivo Excel Correctamente')

