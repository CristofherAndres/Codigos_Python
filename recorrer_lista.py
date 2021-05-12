preferencias = ['Tv','Cine','Paseo','Música','Teatro']

# recorrer forma 1
#for i in range(len(preferencias)):
#    print(preferencias[i])

# recorrer forma 2
#for x in preferencias:
#    print(x)

## Recorrer todos items de la lista e imprimir letra a letra cada items.

###Permite saber el largo de un elemento
#print(len(preferencias))

#Range me genera un intervalo entre 0 y número -1

for i in range(len(preferencias)): # rango 0,1,2,3,4
    print("La palabra N°",i+1,"mide:", len(preferencias[i]))
    for j in range(len(preferencias[i])):
        print(preferencias[i][j])
    print("")

for x in preferencias:
    print("La palabra mide:", len(x))
    for y in x:
        print(y)
    print("")