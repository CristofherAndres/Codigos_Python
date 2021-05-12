print("Elija el Tamaño")
print("---------------")
print("1... Individual")
print("2... Mediana")
print("3... Familiar")

opcion = int(input("Elija el tamaño... "))
if opcion==1:
    pizza = "Individual"
if opcion==2:
    pizza = "Mediana"
if opcion==3:
    pizza = "Familiar"
i=0
ingredientes = []

while(i!=9):
    print("Selecione los ingredientes")
    print("--------------------------")
    print("1... Tomate")
    print("2... Aceituna")
    print("3... Choclo")
    print("4... Espárragos")
    print("5... Pimentón")
    print("9... Ver pizza")
    
    opcion = int(input("Elija su opción... "))
    if opcion==1:
        ingredientes.append("Tomate")
    if opcion==2:
        ingredientes.append("Aceituna")
    if opcion==3:
        ingredientes.append("Choclo")
    if opcion==4:
        ingredientes.append("Espárragos")
    if opcion==5:
        ingredientes.append("Pimentón")
    if opcion == 9:
        print("Su pizza es:",pizza)
        print("lleva:")
        for i in ingredientes:
            print(i)
        break
print("Gracias por su preferencia")
