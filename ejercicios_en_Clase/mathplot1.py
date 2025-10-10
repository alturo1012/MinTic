#instalar mathplotlib
#pip install matplotlib

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#crear datos
productos = ['A', 'B', 'C', 'D']
ventas = [250, 150, 300, 100]

#crear grafica de barras
plt.bar(productos, ventas, color=['blue', 'orange', 'green', 'red'])
plt.title('Ventas por Producto')
plt.xlabel('Productos')
plt.ylabel('Ventas')
plt.show()

#crear datos para grafica de pastel
etiquetas = ['Producto A', 'Producto B', 'Producto C', 'Producto D']
tamaños = [250, 150, 300, 100]
colores = ['blue', 'orange', 'green', 'red']
explode = (0.1, 0, 0, 0)  # separar la primera porción  
plt.pie(tamaños, explode=explode, labels=etiquetas, colors=colores, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')  # Igualar los ejes para que el pastel sea un círculo
plt.show() 