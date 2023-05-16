texto = input("Ingrese un texto: ")
letras = input("Ingrese tres letras separadas por espacios: ").lower().split()

contador_letras = {letra: texto.lower().count(letra) for letra in letras}
print("Cantidad de veces que aparece cada letra:")
for letra, cantidad in contador_letras.items():
    print(f"{letra}: {cantidad}")
    
palabras = texto.split()
print(f"Cantidad total de palabras: {len(palabras)}")

primera_letra = texto[0]
ultima_letra = texto[-1]
print(f"Primera letra: {primera_letra}")
print(f"Última letra: {ultima_letra}")

texto_inverso = texto[::-1]
print(f"Texto en orden inverso: {texto_inverso}")

if "python" in palabras:
    print("La palabra 'python' aparece en el texto.")
else:
    print("La palabra 'python' no aparece en el texto.")