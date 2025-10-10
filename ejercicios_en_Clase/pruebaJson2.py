import pandas as pd

#cargar archivo json
df=pd.read_json("data/pruebajson2.json") 
print("dataframe original")
print(df)

#seleccionar y dividir grupos por dataframe separados para luego unirlos
df1 = pd.DataFrame(df["grupo1"].tolist()) #para convertir una columna de listas en un dataframe
df2 = pd.DataFrame(df["grupo2"].tolist()) #para versiones anteriores de python se usa el .tolist()

print("dataframe grupo 1")
print(df1) 
print("dataframe grupo 2")
print(df2)

#unir los dataframes
df_final = pd.concat([df1, df2], axis=0, ignore_index=True)
print("dataframe final")
print(df_final) 

print(df_final.duplicated) #contar duplicados
print(df_final.duplicated(subset=['Id'])) #ver cuales son los duplicados en la columna ID