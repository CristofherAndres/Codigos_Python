##Usuario ingresa una palabra
palabra = input("Ingrese una palabra o frase:  ")

##lower transforma en minuscula
palabra = palabra.lower()

cont_vocales = 0

for i in palabra:
    if i=='a' or i=='e' or i=='i' or i=='o' or i == 'u':
        cont_vocales +=1

print("La cantidad de vocales son:",cont_vocales)