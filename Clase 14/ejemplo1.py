import sys

num1 = input("Ingresa el primer número: ")
num2 = input("Ingresa el segundo numero: ")


try:
    num1 = int(num1)
    num2 = int(num2)
except:
    print("Al menos un dato es erroneo",file=sys.stderr)
    sys.exit()

resultado = num1+num2
print(resultado)

    




