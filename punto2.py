
numero=int(input("Ingrese un numero para la sumatoria, si quiere finalizar ingrese el 0: "))
def sumadigitos(numero):
    suma = 0
    while numero != 0:
        digito=numero%10
        suma=suma+digito
        numero=numero//10
    return suma

while numero!=0:
    print("suma: ", sumadigitos(numero))
    numero=int(input("Ingrese un numero para la sumatoria, si quiere finalizar ingrese el 0: "))
