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
