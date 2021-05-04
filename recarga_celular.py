import random
import time

#generar saldo aleatorio entre 0 y 3000
#saldo = random.randint(0,3000)
saldo = random.randrange(0,3000+1)

#Validar las opciones ingresadas por el usuario
valida=True
compania=True
mensaje="La compañia es "

#Indicar las compañias
print("1... Entel")
print("2... Movistar")
print("3... Claro")

opcion = int(input("Seleccione una compañia..."))
if opcion==1:
    mensaje += "entel"
elif opcion==2:
    mensaje += "Movistar"
elif opcion==3:
    mensaje += "Claro"
else:
    print("Opción no válida")
    compania = False

if compania:
    print(".")
    print(mensaje,"y su saldo es:",saldo)
    print(".")

    #Ofrecer recarga
    print("1... Recargar 1000")
    print("2... Recargar 2000")
    print("3... Recargar 5000")
    print("------------------")
    opcion = int(input("Seleccione una recarga..."))
    if opcion==1:
        saldo=saldo+1000
    elif opcion==2:
        saldo=saldo+2000
    elif opcion==3:
        saldo=saldo+5000
    else:
        print("Opción no válida")
        valida = False
    if valida:
        print(".")
        print("Recargando...")
        time.sleep(3)
        print("Nuevo saldo $",saldo)
        time.sleep(2)