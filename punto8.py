def primo(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True
def frecuencia(numero,digito):
    cantidad=0
    while numero!=0:
        ultDigito=numero%10
        if ultDigito==digito:
            cantidad+=1
        numero=numero//10
    return cantidad
def factorial(numero):
    f=1
    if numero!=0:
        for i in range(1,numero+1):
            f=f*i
    return f
def sumaDigitos(numero):
    suma=0
    while numero!=0:
        digito=numero%10
        suma=suma+digito
        numero=numero//10
    return suma
mayor=0
agregar = "si"
while agregar == "si":
    numero=int(input("ingrese un numero primo: "))
    while primo(numero):
        digito=int(input("Digitos: "))
        print("suma de los digitos: ",sumaDigitos(numero))
        print("El",digito,"aprece",frecuencia(numero,digito),"veces")
        if numero > mayor:
            mayor=numero
        break
    else:
        print("Factorial de",mayor,":",factorial(mayor))
        print("el ulrimo numero ingresado no es primo.")
        print("el programa ha finalizado con exito")
        break
    agregar = input("¿Quiere ingresar otro numero?\n si o no:\n ")
    if agregar == "no":
        print("factorial de",mayor,":",factorial(mayor))
        print("El programa ha finalizado con exito.")
        break



