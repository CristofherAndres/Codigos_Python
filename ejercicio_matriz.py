import numpy as np
import random as rd

m = int(input("Ingrese el tamaño M de su matriz MxN:  "))
n = int(input("Ingrese el tamaño N de su matriz MxN:  "))

matriz = np.zeros((m,n))

for i in range(m):
    for j in range(n):
        matriz[i][j] = rd.randint(1,100)

print(matriz)

if n==m:
    print("La matriz es cuadrada")
else:
    print("La matriz no es cuadrada")

suma = 0
for i in range(m):
    for j in range(n):
        suma += matriz[i][j]

print("El promedio es:",suma/(n*m))

suma = 0
for i in range(m):
    for j in range(n):
        suma += matriz[i][j]
    print("El promedio de la fila",i,"es:",suma/(n))
    suma = 0

suma = 0
for i in range(n):
    for j in range(m):
        suma += matriz[j][i]
    print("El promedio de la columna",j,"es:",suma/(m))
    suma = 0

    21.75