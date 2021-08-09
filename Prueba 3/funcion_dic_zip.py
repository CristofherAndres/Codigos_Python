
#### función DICT

dic = dict(nombre="Pedrito", apellido="Perez", edad=7)

print(dic)

print(dic["nombre"])


#### función ZIP

dic = dict(zip('abcdefghijklmnopqrstuvwxyz',range(1,27)))

items = dic.items()

print(items)


##### Metodo KEY

claves = dic.keys()
print(claves)

valores = dic.values()
print(valores)

##### CLEAN

#dic.clear()
#print(dic)

##### COPY

dic2 = dic.copy()

print(dic2)

dict = dic.fromkeys(['a','b','c'],1)
print(dict)


valor = dic.get('j')

print(valor)