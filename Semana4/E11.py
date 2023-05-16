def contar_vocales(cadena):
    vocales = 'aeiouAEIOU'
    contador = 0
    for letra in cadena:
        if letra in vocales:
            contador += 1
    return contador

texto = input("Ingrese una cadena de texto: ")
num_vocales = contar_vocales(texto)
print("El número de vocales en la cadena es:", num_vocales)