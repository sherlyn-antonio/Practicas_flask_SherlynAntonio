#creando un diccionario 
persona={
    "Nombre":"Sherlyn",
    "Edad":15,
    "Profesion":"programador",
    "Estudiante":True
}
print(persona)
#accediendo a un valor especifico
print(persona["Nombre"])
#se puede usar el metodo get()
#es util por que no marca error si el valor no existe
print(persona.get("Profesion"))
#modificar un valor existente
persona["Edad"]=15
print(persona["Edad"])
#Agregar un par (clave:valor)
persona["ciudad"]="San Pepe ranch"
print(persona)
#Recorrer un diccionario con un bucle