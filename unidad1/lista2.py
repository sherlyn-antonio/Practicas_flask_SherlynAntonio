# Declarando dos listas
try:
    alumnos = ["Mariel", "Sherlyn", "Melisa", "Ximena", "Dulce"]
    calificaciones = [9, 8, 10, 7, 9]

    print("Lista de alumnos:", alumnos)
    print("Lista de calificaciones:", calificaciones)

    print("Alumnos con índices impares:")

    print(alumnos[1])
    print(alumnos[3])
except IndexError:
    print("indice incorrecto")