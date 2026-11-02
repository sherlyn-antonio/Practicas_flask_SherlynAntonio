promedio=float(input("ingresa el promedio:"))
#el numero ingresado es 6
if promedio<=-5:
    print("ese promedio no existe")
elif promedio>=0 and promedio<=5:
    print("tu promedio es bajo")
elif promedio>=5 and promedio<=7:
    print("tu promedio es muy bajo")
elif promedio>=7 and promedio<=9:
    print("tu promedio es bueno")
elif promedio>9 and promedio<=10:
    print("tu promedio es excelente")
else:
    print("ese promedio no existe")