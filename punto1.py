def validar(email):
    b=correo.count("@")
    if b==1:
        return True
    return False    

correo=input("introduce tu correo electronico: ")
if validar(correo):
    print("Tu correo electronico es valido :)")
else:
    print("Tu correo electronico es invalido :(")
    print("Por favor ingrese su correo electronico con un @")    