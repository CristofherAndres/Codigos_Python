cont = 1

while cont:
    print(cont)
    cont+=1
    if cont==25:
        break

cont = 0
while cont < 10:
    cont+=1
    
    if cont%2==0:
        continue
    print(cont, end=" ")
    print("Es impar")
