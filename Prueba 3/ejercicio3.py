def validar_nombre(nombre):
    if len(nombre)<6:
        return "El nombre de usuario debe contener al menos 6 caracteres"
    if len(nombre)>12:
        return "El nombre de usuario no debe contener más de 12 caracteres"
    if " " in nombre:
        return "El nombre no puede contener espacios"
    if nombre.isalpha:
        return "Nombre de usuario correcto"

############################################

nombre = input("Ingrese un nombre de usuario: ")
print(validar_nombre(nombre))
