# numeros [10,8,45,26,7] hacer una funcion que halle el maximo, el minimo y la suma

numeros = [10,8,45,26,7]

def funciones (a):
    m = max(a)
    n = min(a)
    producto = 0
    for i in a:
        producto = producto + i
    return print(f"el numero mayor de la lista es: {m}, el menor es: {n} y la suma total es: {producto}")

print(funciones(numeros))

def funciones2 (a):
    q = max(a)
    w = min(a)
    e = sum(a)
    return print(f"el numero mayor de la lista es: {q}, el menor es: {w} y la suma total es: {e}")

print(funciones(numeros))

funciones3 = lambda a : print(f"la lista es {sorted(a)}, el numero mayor de la lista es: {max(a)}, el menor es: {min(a)} y la suma total es: {sum(a)}")

print(funciones3(numeros))