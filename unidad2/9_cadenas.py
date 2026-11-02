#cadenas y concatenacion con (+)
cadena1='Hola'
cadena2='Mundo'
multilinea="""Esto es una cadena
de varias lineas""" 
print(cadena1 + cadena2 + multilinea)
eco="ja"*3
print(eco)
#cambiar una cadena de minuscula a mayusculas 
tu_nombre='sherlyn' 
print(tu_nombre.upper())
#cambiar una cadena de mayuscula a minuscula
print(tu_nombre.lower())
#remplazar texto en una cadena 
frase="Me gusta programacion"
print(frase.replace("programacion","Ingles"))
#formato de cadenas(f-string)
edad=15
Nombre='Sherlyn'
mensaje=f"Hola, me llamo {Nombre} y tengo {edad} años"
print(mensaje)
#Contar los caracteres de una cadena
texto="¡Felicidades por aun continuar en el CECY!"
print(texto)
cantidad_caracteres=len(texto)
print(cantidad_caracteres)
#Comprobar si un texto contiene una palabra 
oracion="Aprender python es divetido"
if "java" in oracion:
    print("Encontrado")
else:
    print("No esta")
#Validar contenido de una cadena
nlista="1"
print(nlista.isalpha())
print(nlista.isdigit())