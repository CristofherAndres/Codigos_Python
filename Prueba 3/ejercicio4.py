def validar_contrasena(contrasena):

    mayu=0
    mini=0
    nume=0
    espacio=0

    if len(contrasena) < 6:
        return "Debe contener al menos 6 caracteres"
    elif len(contrasena) > 12:
        return "Debe contener máximo 12 caracteres"
    else:
        for letra in contrasena:
            if letra.islower():
                mini+=1
            elif letra.isupper():
                mayu+=1
            elif letra.isnumeric():
                nume+=1
            elif letra.isspace():
                espacio+=1

        if (mini>0 and mayu>0 and nume>0 and espacio == 0):
            return "Contraseña segura"
        else:
            return "Contraseña no valida"

#################################################

contra = input("Indique su contraseña:  ")
print(validar_contrasena(contra))
