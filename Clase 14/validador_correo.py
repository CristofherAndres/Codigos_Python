def val_correo(texto):
    validador=0
    
    for i in range(len(texto)):
        if texto[i]=='@':
            validador=validador+1

    if validador==1:
        return True
    else:
        return False

###############################

correo = input("Ingrese su correo: ")

if val_correo(correo):
    print("Correo valido")
else:
    print("Correo invalido")

    
