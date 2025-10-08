#crear una lista de 15 numeros aleatorios entre 1 y 50 y mostrar en una nueva lista los pares e impares 
# adicional si el numero 32 se encuentra encuentra entre la lista 
import random

lista = []
pares = []
impares = []

for elemento in range(15):
    lista.append(random.randint(1,50))

print(lista)
print(sum(lista))
print(max(lista))
print(min(lista))
prom = sum(lista)/len(lista)
print(prom)
print(lista[::-1])#accede la lista pero en reversa 
print(lista[-1])
print(set(lista))#elimina duplicados y ordena
print(f"Numeros ordenados{sorted(lista)}") #ordena la lista
print(f"numeros ordenados decendentemente{sorted(lista, reverse= True)}")#ordena decendentemente

for elemento in lista:
    if elemento%2 == 0:
        pares.append(elemento)
    else:
        impares.append(elemento)

print(pares)
print(impares)

elemento_buscar = 32
if elemento_buscar in lista:
    print("encontrado")
else:
    print("no encontrado")


