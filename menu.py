import random
import time

#generar saldo aleatorio entre 0 y 3000
saldo = random.randint(0,3000)
valida=True

print(".")
print("Su saldo es:",saldo)
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