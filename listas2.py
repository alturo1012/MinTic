import random;

frutas = ["uva", "pera", "manzana", "banano"]
print(frutas[-1]) #con el -1 se accede al ultimo elemneto de la lista 

del frutas[2] #eliminar el elemento manzana 
print(frutas)

#recorrer toda la lista elemento por elemento
for elemento in frutas:
    print(elemento)

frutas = ["uva", "pera", "manzana", "banano"]
elemento_buscar = "manzana"
encontrado = False
for elemento in frutas:
    if elemento == elemento_buscar:
        print("elemento encontrado")
        encontrado = True
    else:
        print("elemento no encontrado")
        encontrado = False
        
#contar elementos de lista 
print(f"La lista de frutas contiene {len(frutas)} elementos")
f_corta = [f for f in frutas if len(f)<=4]
print(f"la lista cuenta con {len(f_corta)} frutas con nombres cortos")
print(f"las frutas con nombres cortos son: {f_corta}")

f_corta2 = []
for f in frutas:
    if len(f) <= 4:
        f_corta2.append(f)
        
n = random.randint(1,10)
print(n)