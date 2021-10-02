cond="si"
def frecuencia(numero):
    cantidad=0 
    while numero!=0:
        ultDigito=numero%10
        cantidad+=1
        numero=numero//10
    return cantidad
while cond=="si":
    hi=input("que desea ingresar?\n1.Cedula de ciudadania\n2.Tarjera de identidad\n")
    num=int(input("ingrese el numero: "))
    if frecuencia(num)<4 and frecuencia(num)<12:
        print("el numero es invalido")
    else:
        print("numero es valido")
        cond="no"
    cond=input("¿quieres volver a ingresar?\n¿si o no?\n")
    if cond == "no":
        print("vuelve pornto amigo")