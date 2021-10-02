cond = "si"
def primo(num):
    for x in range(2,num):
        if num%x==0:
            return False
    return True          

while cond == "si":
    numero=int(input("ingrese un numero entero postivo: "))
    if primo(numero):
        print(numero, "es un numero primo")
    else:
        print(numero, "No es un numero primo")
    cond=input("quieres ingresar otro numero?\nResponder si o no\n")
    if cond == "no":
        print("Hasta luego.") 



