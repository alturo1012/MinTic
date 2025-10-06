productos=[
    {"nombre":"manzana","categoria":"frutas","valor":500},
    {"nombre":"pera","categoria":"frutas","valor":200},
    {"nombre":"melocoton","categoria":"frutas","valor":1000},
    {"nombre":"espinaca","categoria":"verdura","valor":700},
    {"nombre":"pan rollo","categoria":"pan","valor":300},
    {"nombre":"zanahoria","categoria":"verdura","valor":1500}
]
print(productos)
#agrupar productos por categoria

agrupados={}
for producto in productos:
    cat=producto["categoria"]
    if cat not in agrupados:
        agrupados[cat]=[]
    agrupados[cat].append(producto["nombre"])
    agrupados[cat].append(producto["valor"])
    agrupados[cat].append({producto["nombre"],producto["valor"]})
    
print(agrupados)

#comentario

