persona={
    "nombre":"mauricio",
    "edad":42,
    "ciudad":"chiquinquira"
}

print (persona["edad"])
persona["nombre"]="juanito"
print(persona)
persona["profesion"]="ingeniero"
print(persona)
print(persona.keys())##es para mirar la informacion que tenemos principal
data2={
    "estrato":2,
    "eps":"nueva eps",
    "comidas":["pasta", "mexican food"],
    "profesion":'carnicero',
    "direccion":{
        "calle":"17B sur",
        "numero":"26-05",
        "complemento":"casa primer piso"
    }
}
persona.update(data2)
print(persona)
print(f"nombre: {persona["nombre"]} casa: {persona["direccion"]}")
print(f"nombre: {persona["nombre"]} casa: {persona["direccion"]["complemento"]}")
print(f"segunda comida:{persona["comidas"][1]}")

productos=[
    {'nombre':'manzana', 'categoria': 'fruta', 'valor': 500},
    {'nombre':'pan rollo', 'categoria': 'pan', 'valor': 600},
    {'nombre':'pera', 'categoria': 'fruta', 'valor': 200},
    {'nombre':'espinaca', 'categoria': 'verdura', 'valor': 500},
    {'nombre':'guineo', 'categoria': 'fruta', 'valor': 300},
    {'nombre':'zanahoria', 'categoria': 'verdura', 'valor': 500}
]
#agrupar productos por categoria
agrupados={}
for producto in productos:
    cat=producto['categoria']
    if cat not in agrupados:
        agrupados[cat]=[]
    agrupados[cat].append([producto['nombre'],producto ['valor']])#agregamos el valor del prodcto a nuestro archivo final, mediante un agrupamiento de datos
    agrupados[cat].append([producto['nombre']])
    agrupados[cat].append([producto['valor']]) #agregar datos pero sin agruparlos. 
print(agrupados)