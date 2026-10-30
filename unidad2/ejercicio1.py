num=int(input("ingresa el numero:"))
if num>=1 and num<=10:
    for i in range(1,11):
        resultado=num*i
        print(num,"x",i,"=",num*i)
else:
    print("ese numero no existe")