#Declarando una lista
try:
    materias=["programacion","filosofia ","matematicas","ingles"]
    print(materias[3])
    materias.append("lengua y comunicacion")
    print(materias)
    materias[1]="Biologia"
    print(materias)
    materias.remove("matematicas")
    print(materias)
except IndexError:
    print("¡no existe ese rango!" )