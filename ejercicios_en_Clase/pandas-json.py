import pandas as pd

#leer archivo json 
df=pd.read_json("data/personas.json")
#imprimir el dataframe
print(df)
#normalizar el json
f_normalizado = pd.json_normalize(df['Estudios'])
#df_normalizado = pd.concat([df.drop(columns="Estudios")])