
Lista=[]
Letras = []

palabra = input("Ingrese una palabra o frase: ")
palabra = palabra.lower().strip()

Lista.extend(palabra)
for i in Lista:
    if (i in Letras) != True:
        Letras.append(i)

print("La cantidad de letras diferentes usadas es: ",len(Letras))


#CONTAR TODOS LAS LETRAS DIFIERENTES DE UNA PALABRA