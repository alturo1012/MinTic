print("Bievenidos al entorno de calificacion")
calificacion1=float(input("ingrese la calificacion del primer estudiante:"))
calificacion2=float(input("ingrese la calificacion del segundo estudiante:"))
calificacion3=float(input("ingrese la calificacion del tercer estudiante:"))
promedio=((calificacion1+calificacion2+calificacion3)/3)

if calificacion1>= 4.5:
    print("su calificacion es A.")
elif calificacion2>= 4.5:
    print("su calificacion es A.")
elif calificacion3>= 4.5:
    print("su calificacion es A.")
elif calificacion1 >= 4:
    print("su calificacion es B.")
elif calificacion2>= 4:
    print("su calificacion es B.")
elif calificacion3>= 4:
    print("su calificacion es B.")
elif calificacion1>= 3.5:
    print("su calificacion es C.")
elif calificacion2>= 3.5:
    print("su calificacion es C.")
elif calificacion3>= 3.5:
    print("su calificacion es C.")
elif calificacion1>=3:
    print("su calificacion es D.")
elif calificacion2>= 3:
    print("su calificacion es D.")
elif calificacion3>= 3:
    print("su calificacion es D.")
else:
    print("su calificacion es F y reprobo la materia.")
print(f"el promedio de notas del curso es: {promedio}")