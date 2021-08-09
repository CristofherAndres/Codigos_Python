
import numpy as np
import random as rd

n = int(input("Ingrese el tamaño de su matriz nxn:  "))

matriz = np.zeros((n,n))


print(matriz)

for i in range(n):
    for j in range(n):
        matriz[i][j] = rd.randint(1,100)

print(matriz)

mayor = 0
menor = 101

for i in range(n):
    for j in range(n):
        if mayor < matriz[i][j]:
            mayor = matriz[i][j]
        elif menor > matriz[i][j]:
            menor = matriz[i][j]

print("El dato mayor de la matriz es: ",mayor)
print("El dato menor de la matriz es: ",menor)