lista = [1,2,3,4,5,6]

del lista[3]
print(lista)


lista.append(99)
print(lista)

lista.insert(2,10)
print(lista)


lista.insert(100,66)
print(lista)


tope_pila=lista.pop()
print(tope_pila)
print(lista)

lista.reverse()
print(lista)

lista.sort()
print(lista)