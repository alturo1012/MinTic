import pandas as pd 

#cargar los dataframes de ventas y productos

ventas = pd.read_csv('Data/ventas1.csv', sep=',', encoding='utf-8')
productos = pd.read_csv('Data/productos.csv', sep=',', encoding='utf-8')

print("Datos de ventas:")
print(ventas.head())
print("Datos de productos:")
print(productos.head())

#establecer la columna "producto id" como indice de en ambos dataframes

ventas.set_index("Producto_ID", inplace=True)
productos.set_index("Producto_ID", inplace=True)

#fusionar los data frames utilizando el metodo adecuado (.join()) o pd.merge()).

df_combinado = ventas.join(productos, how = "inner")
print("Datos fusionados: ")
print(df_combinado.head())
 
df_combinado["Ingrsos totales"] = df_combinado["Cantidad Vendida"] * df_combinado["Precio Unitario"]

print(df_combinado.head(10))