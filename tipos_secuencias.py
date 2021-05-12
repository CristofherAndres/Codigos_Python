#tuplas - No Eliminar - No modificar - No agregar
tupla = (1,2,3,4,'Hola mundo')

for i in tupla:
    print(i)

#Listas - Eliminar - Modificar - Agregar
Lista = [1,2,3,4,'Hola mundo']

#Una forma de imprimir una lista
for i in Lista:
    print(i)

Lista[0] = 'Modificado'

for i in Lista:
    print(i)


#Diccionarios

diccionario = {"Papa":350,"Manzana":500,"naranja":350}

for i in diccionario.items():
    print(i)
