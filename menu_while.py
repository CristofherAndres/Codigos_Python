nombre = input("Ingrese su nombre: ")
mensaje = "Bienvenido xxxxxx, ¡que tengas una excelente tarde!"
mensaje = mensaje.replace("xxxxxx",nombre)
print(mensaje)

opcion = 1

while opcion == 1:
    print("¿Desea realizar otra operación?...")
    print("1...SI")
    print("2...NO")
    opcion=int(input("Ingrese su opción..."))