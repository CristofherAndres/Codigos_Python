def suma(list):
    suma = 0
    for i in list:
        suma=suma+i
    return suma



Lista = []

for i in range(5):
    Lista.append(int(input("Ingrese un número: ")))

print(Lista)

print(suma(Lista))