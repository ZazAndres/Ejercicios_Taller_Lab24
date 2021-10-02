from typing import Sized


cond="si"
def frecuencia(numero,digito):
    cantidad=0
    while numero !=0:
        ultDigito=numero%10
        if ultDigito==digito:
            cantidad+=1
        numero=numero//10
    return cantidad
while cond=="si":
    num=int(input("ingrese un numero: "))
    un_digito=int(input("ingrese un digito: "))
    print("frecuencia del digito en el numero:",frecuencia(num,un_digito))
    cond=input("¿Quieres volver a ingresar un numero y un digito?\n¿Si o no?\n")
    if cond=="no":
        print("vuelve pronto amigo")
