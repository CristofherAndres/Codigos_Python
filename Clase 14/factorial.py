def factorial(num):
    f=1
    i=1
    while i<=num:
        f=f*i
        i=i+1
    return f

#############################
import sys as s
num = input("Ingrese un número: ")

try:
    num = int(num)
    
except:
    print("El número ingresado no es valido",file=s.stderr)
    s.exit()

if (num>=0):
    print(factorial(num))
else:
    print("El número ingresado no es valido")