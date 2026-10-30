#Creando una matriz
numeros=[
    [1,2,3],
    [2,3,4],
    [5,6,7]
]
#Obteniendo el numero total de filas 
filas=len(numeros)#filas=3
#Obteniendo el numero total de columnas
columnas=(numeros[0])
#Ciclo externo para los inidices de las filas(i)
for i in range(filas):
    #Ciclo interno para los indices de las columnas(j)
    for j in range(columnas):
        print(f"[{i}][{j}] = {numeros[i][j]}")