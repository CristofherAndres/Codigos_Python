def palindromo(palabra):
    palabra = palabra.replace(" ","")
    palabra = palabra.replace(".","")
    palabra = palabra.replace(",","")
    palabra = palabra.replace("-","")
    palabra = palabra.lower()
    alreves=palabra[len(palabra)::-1]

    if palabra==alreves:
        return True
    return False

#########################################

frase = input("Ingrese una frase: ")

if palindromo(frase):
    print("La palabra o frase ingresa es palindromo")
else:
    print("La palabra o frase ingresa no es palindromo")
