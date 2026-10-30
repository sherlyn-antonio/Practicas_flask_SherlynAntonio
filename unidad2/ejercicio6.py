tabla=[
    ["nombre","edad","calificacion"],
    ["darina",16,9.0],
    ["valeria",16,8.0],
    ["dulce",16,9.5],
    ["carlos",16,8.0],
    ["oscar",16,7.0],
    ["mariel",16,9.4],
    ["jorge",16,6.0],
    ["jesus",16,7.0],
    ["melisa",16,8.0],
    ["ximena",16,9.0]
]
filas = len(tabla)
columnas = len(tabla[0])

buscar_alumno = input("Ingresa el nombre del alumno: ")
for i in range(filas):
    for j in range(columnas):
        if j == 0 and tabla[i][j] == buscar_alumno:
            print(f"Alumno encontrado en la posicion = [{i}][{j}]")