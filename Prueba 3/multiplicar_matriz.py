#import numpy as np

matriz1 = ((1,2),(3,4),(5,6))
matriz2 = ((1,2,3),(4,5,6))

matriz_resultado = ((0,0,0,),(0,0,0),(0,0,0))

#matriz_resultado = np.zeros((3,3))

print(matriz_resultado)


for i in range(len(matriz1)):
    for j in range(len(matriz1[0])-1):
        for k in range(len(matriz2)-1):
            for l in range(len(matriz2[0])):
                print(matriz1[i][j],"*",matriz2[k][l], end=' - ')
                print(matriz1[i][j+1],"*",matriz2[k+1][l], end=' ')
            print()
