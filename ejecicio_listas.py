frutas = ["platano","manzana","naranja"]

while True:
    tu_fruta = input("(FIN...SALE, M...Muestra) \n Ingresa la fruta... ")
    tu_fruta=tu_fruta.lower()

    if tu_fruta=="fin":
        break
    if tu_fruta=="m":
        for i in frutas:
            print(i)
    
    if tu_fruta in frutas:
        print("La fruta ya existe, agrega otra")
    elif tu_fruta!="m":
        frutas.append(tu_fruta)
    else:
        print("---")