contrasena_valida = 'IntroProgra'

contrasena_usuario = input("Ingrese la contraseña: ")

if contrasena_valida == contrasena_usuario:
    print("Contraseña correcta")
else:
    contrasena_usuario = input("Ingresaste una contrseña invalida, intentalo nuevamente: ")
    if contrasena_valida == contrasena_usuario:
        print("Contraseña correcta")
    else:
        print("Contraseña incorrecta")