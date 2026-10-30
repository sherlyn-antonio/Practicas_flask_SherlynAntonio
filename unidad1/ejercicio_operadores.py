[4:50 p.m., 29/10/2026] ঌ 𝑺𝒉𝒆𝒓 ໒꒱: #Sherlyn Antonio Garcia
colores=["morado","rojo","blanco","verde"]
print("rojo" in colores)
print(len(colores))
print(colores+["verde"])
print(colores*2)
[4:50 p.m., 29/10/2026] ঌ 𝑺𝒉𝒆𝒓 ໒꒱: #realizar un programa que calcule
#la compra total de 4 productos, si la compra total
#es mayor a 2000 pesos me haga un descuento
#del 10%
#DATOS DE ENTRADA
precio1=float(input("introduce el precio del producto 1:"))
precio2=float(input("introduce el precio del producto 2:"))
precio3=float(input("introduce el precio del producto 3:"))
precio4=float(input("introduce el precio del producto 4:"))
#proceso
total=precio1+precio2+precio3+precio4
if total>2000:
    total=(total-(total*.10))
    #total=(300-(total*.10)) total=2700
    print(total)
else:
        print("NO TIENES DESCUENTO")