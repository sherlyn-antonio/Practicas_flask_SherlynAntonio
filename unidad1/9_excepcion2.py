try:
    numero1=float(input("ingresa el primer numero:"))
    numero2=float(input("ingresa el segundo numero:"))
    resultado=numero1/numero2
except ValueError:
    print("solo introduce numeros")
except ZeroDivisionError:
    print("division entre cero")
else:
    print("El resultado es ",resultado)
finally:
    print("Programa finalizado")