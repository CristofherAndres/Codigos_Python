Frase = input("Ingrese una frase: ")
i=0
cant_a=0

while (i<=len(Frase)-1):
    if(Frase[i]=='a' or Frase[i]=='A'):
        cant_a+=1
    i+=1

print("La frase tiene",len(Frase),"letras")
print("La cantidad de A:",cant_a)
