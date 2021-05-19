import math as m

print("Recuerda ir ingresando números enteros cada vez más grandes")

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
suma = num1+num2

while num2 <= num1:
    num2 = int(input("Ingrese nuevamente el segundo número: "))

limite = int(input("Ingresa el limite del juego: "))

mayor = num2
while suma < limite:
    num_actual = int(input("Ingrese un número: "))
    
    while mayor >= num_actual:
        num_actual = int(input("Ingrese nuevamente el número: "))

    mayor = num_actual
    suma += num_actual

print("El limite es:",limite)
print("La suma es:",suma)


# Parte en 1 hasta la suma
for i in range(1,suma+1):
    if (i % 5 == 0) and (i % 7 == 0):
        print("Divisible por 5 y 7:",i)

##Todos los digitos diferentes
for i in range(100,suma+1):
    if i<1000:
        num = i
        cent = m.trunc(num/100)
        num = num%100
        dec = m.trunc(num/10)
        uni = num%10
        if cent!=dec and cent!=uni and dec!=uni:
            print("Número de 3 cifras diferentes",i)
    else:
        break

##Todos los digitos diferentes
for i in range(100,suma+1):
    if i<1000:
        num = i
        cent = m.trunc(num/100)
        num = num%100
        dec = m.trunc(num/10)
        uni = num%10
        if cent%2==0 and cent%2==0 and uni%2==0:
            print("Número de 3 cifras pares",i)
    else:
        break


    