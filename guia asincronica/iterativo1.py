contrasena_valida = 'IntroProgra'
contrasena_usuario = input("Ingrese la contraseña: ")

cont = 1

while contrasena_usuario!=contrasena_valida and cont<3:
    print("Contraseña erronea, intentelo nuevamente...")
    contrasena_usuario = input("Ingrese la contraseña: ")
    cont+=1

if contrasena_valida == contrasena_usuario:
    print("Contraseña correcta")
    cont-=1
    print("Lo lograste en",cont+1,"intentos")

if cont >= 3:
    print("Sistema bloqueado, muchas veces has puesto la contraseña erronea")
