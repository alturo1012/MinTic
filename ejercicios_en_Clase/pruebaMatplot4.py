import matplotlib as mpl

ingresos = [1200, 1500, 1700, 1600, 1800, 2000]
gastos = [800, 700, 900, 850, 950, 1000]

mpl.scatter(ingresos, gastos, color='purple', marker='x')
mpl.title('Relación entre Ingresos y Gastos')
mpl.xlabel('Ingresos')
mpl.ylabel('Gastos')
mpl.grid()
mpl.show()

