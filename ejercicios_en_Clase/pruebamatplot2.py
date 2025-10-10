import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio']
ventas = [200, 220, 250, 300, 280, 320]

plt.plot(meses, ventas, marker='o', linestyle='-', color='b')
plt.title('Ventas Mensuales')
plt.xlabel('Meses') 
plt.ylabel('Ventas')
plt.grid()  
plt.show()

 