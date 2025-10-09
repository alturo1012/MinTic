import pandas as pd

#leer archivo json 
df=pd.read_json("data/personas.json")
#imprimir el dataframe
print(df)