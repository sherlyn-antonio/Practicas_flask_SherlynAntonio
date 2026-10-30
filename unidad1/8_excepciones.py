#Ejemplo 1 sin manejo de excepciones
try:
    numero1=float(input("INGRESAR EL PRIMER NUMERO:"))
    numero2=float(input("INGRESAR EL SEGUNDO NUMERO:"))
    resultado=numero1/numero2
    print(resultado)
except ZeroDivisionError:
     print("NO SE PUEDE DIVIDIR ENTRE CERO")
except ValueError:
    print("error no se puede ingresar letras")