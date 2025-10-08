print("Bievenidos al entorno de calificacion")
calificacion=int(input("ingrese la calificacion del estudiante"))

if calificacion >= 90:
    print("su calificacion es A.")
elif calificacion >= 80:
    print("su calificacion es B.")
elif calificacion >= 70:
    print("su calificacion es C.")
elif calificacion >-60:
    print("su calificacion es D.")
else:
    print("su calificacion es F.")