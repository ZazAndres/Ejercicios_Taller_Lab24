cond="si"
def sumaDigitos(numero):
    suma=0
    while numero!=0:
        digito=numero%10
        suma=suma+digito
        numero=numero//10
    return suma
cantidad=0
mayor=-1
numero=int(input("Numero positivo:"))
while cond=="si":
    if numero>=0:
        while numero>=0:
            suma=sumaDigitos(numero)
            if suma > mayor:
                n_mayorsuma=numero
            if suma < 10:
                cantidad +=1
            print("Sumatoria de digitos de",n_mayorsuma,":",mayor)
            print("cantidad con sumatoria menor a 10:", cantidad)
            cond==input("¿quiere ingresar otro valor?\n¿si o no?\n")
            numero=int(input("numero positivo: "))
    else:
        print("el numero ingresado es incorrecto")
        cond=="si"