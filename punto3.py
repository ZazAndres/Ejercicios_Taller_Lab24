numero=int(input("Ingrese un numero para la sumatoria, si quiere finalizar ingrese el 0: "))
def sumadigitos(numero):
    suma = 0
    while numero != 0:
        digito=numero%10
        suma=suma+digito
        numero=numero//10
    return suma

sumatoria=0
while numero!=0:
    sumatoria=sumatoria+numero
    print("suma: ", sumadigitos(numero))
    numero=int(input("Ingrese un numero para la sumatoria, si quiere finalizar ingrese el 0: "))

print("La sumatoria de todos los numeros ingresados es: ", sumatoria)
print("La sumatoria de los digitos de los numeros ingresados es: ", sumadigitos(sumatoria))