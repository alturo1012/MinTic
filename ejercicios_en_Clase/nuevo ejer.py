import numpy
lista=[1,2,3]
my_array= numpy.array(lista)
print(f"lista {lista}")
print(f"arreglo {my_array}")
b=lista+my_array
print(f"combinar {b}")
array_lista = my_array.tolist()
union= array_lista+ lista
print(f"arreglo del arreglo a lista {array_lista}")
print(f"union de las listas {union}")
