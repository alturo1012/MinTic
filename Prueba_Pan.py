import pandas as pa 

serie = pa.Series([10,20,30], index = ["A", "B", "C"])
print(serie)
print(serie['B'])

datos = {
    'Nombre':['Juan', 'Ana', 'Milena'],
    'Edad': [15,25,32],
    'Ciudad': ['Bogota', 'Cali', 'Medellin']
}

dataF = pa.DataFrame(datos)
print(dataF)

serie = pa.Series([100, 200, 300, 400, 500], index = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"])

print(serie["Miercoles"])

promedio = serie.mean()

print(promedio)

for i in serie:
    serie2 = serie + 50

print(serie2)

import pandas as pa 

serie = pa.Series([100, 200, 300, 400, 500], index = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"])

print(serie["Miercoles"])

promedio = serie.mean()

print(promedio)

serie = serie + 50

print(serie)