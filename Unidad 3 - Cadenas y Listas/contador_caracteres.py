frase = input("Ingrese una frase... ")

print(frase)
largo = len(frase)
print("El largo de la frase es:",largo)

frase = frase.strip()
print(frase)

cont = 0

for i in frase:
    cont=cont+1
    if i.isspace():
        cont=cont-1
        
print("El largo de la frase sin espacios es:",cont)

largo= len(frase)
espa = 0
for i in frase:
    if i.isspace():
        espa=espa+1

print("El largo de la frase sin espacios es:",largo-espa)        

