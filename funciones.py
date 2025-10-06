def suma(a,b):
    sum = a + b
    return sum


print(suma(4,6))

def saluda(nom):
    return print(f"hola {nom}")

def cuadrado(n):
    return n ** 2

numero = cuadrado(2)
print(f"el resultado es: {numero}")


def cambia(d,o):
    r = []
    for i in d:
        if i is None:
            r.append(o)
        else:
            r.append(i)
    return r

datos = [1, None, 2, None, 3]

print(cambia(datos, 0))

suma2 = lambda x,y: x+y

print(suma2(4,1))

cambia2 = lambda datos,p : [p if i is None else i for i in datos]
print(cambia2(datos,0))

