def factorial(numero):
    f=1
    if numero !=0:
        for i in range(1,numero+1):
            f=f*1
    return f
cantidad=0
num=int(input("ingrese un numero, si quiere terminar ingrese un -1 para cortar: "))
while num!=-1:
    print("factorial:", factorial(num))
    cantidad+=1
    num=int(input("ingrese un numero, si quiere terminar ingrese un -1 para cortar: "))
print("se leyeron", cantidad, "numeros ingresados")