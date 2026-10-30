num=int(input("ingresa el numero:"))
if num>=1 and num<=10:
    i=1
    while i<= 10:
        resultado=num*i
        print(num,"x",i,"=",num*i)
        i=i+1
else:
    print("ese numero no existe")