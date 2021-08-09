import numpy as np

m = int(input("Ingrese el tamaño M de su matriz MxN:  "))
n = int(input("Ingrese el tamaño N de su matriz MxN:  "))

K = int(input("Ingrese el valor K para multiplicar la matriz:  "))

matriz = np.zeros((m,n))

print(matriz)

for i in range(m):
    for j in range(n):
        matriz[i][j] = int(input("Ingrese el dato ("+str(i)+","+str(j)+"): "))

    
print(matriz)

for i in range(m):
    for j in range(n):
        matriz[i][j] *= K

print(matriz)

Construir una matriz N x M

1) Indicar si es cuadrada
2) mostrar el promedio de la matriz
3) mostrar el promedio de cada fila
4) mostrar el promedio de cada columna