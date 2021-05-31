num = int(input("Ingrese un numero: "))

if num > 0:
    if num%3==0:
        print("Número positivo y divisible por 3")
    else:
        print("Número positivo y No es divisible por tres")
else:
    if num%3==0:
        print("No es número positivo y divisible por 3")
    else:
        print("No es número positivo y No es divisible por tres")