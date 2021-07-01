#Lista vacia
Lista = []
print(Lista)

Lista2 = [1,2,3,3,3,3,7]
print(Lista2)

print(Lista2[3])

Lista2[3] = "Cambio"
print(Lista2)

#Lista[0] = "Nuevo dato"

Lista.append("Nuevo dato")

print(Lista)
Lista[0] = "Cambio"

Lista2.insert(2,99)
print(Lista2)


Lista2.insert(99,999)
print(Lista2)

Lista2.insert(2,66)
print(Lista2)

Lista2.insert(2,67)
print(Lista2)

Lista2.insert(2,68)
print(Lista2)

Lista2.insert(98,666)
print(Lista2)

Lista.extend("Lista2")
print(Lista)

### PILA

#AGREGAR DATOS - FINAL
#SACAR DATOS - FINAL

print("###########",end="\n\n\n")

Lista.append("Nuevo dato Pila")
print(Lista)

dato = Lista.pop()
print(dato)
print()
print(Lista)


### COLA

#AGREGAR DATOS - FINAL
#SACAR DATOS - PRIMERO

print("Cola")

Lista.append("Nuevo dato COLA")
print(Lista)

dato = Lista[0]
print(dato)
del Lista[0]

print(Lista)

Lista.sort()

print(Lista)