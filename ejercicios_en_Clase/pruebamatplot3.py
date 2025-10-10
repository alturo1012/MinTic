import matplotlib.pyplot as plt
import numpy as np      
import pandas as pd
import json

edades = [23, 45, 56, 78, 89, 90, 34, 23, 45, 67, 89, 90, 21, 34, 56, 78, 89, 90]
plt.hist(edades, bins=10, color='blue', edgecolor='black')
plt.title('Distribución de Edades')
plt.xlabel('Edades')
plt.ylabel('Frecuencia')
plt.show()
