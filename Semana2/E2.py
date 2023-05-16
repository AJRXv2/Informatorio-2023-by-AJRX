#-Escribir un programa que pida al usuario un número entero y muestre por 
#pantalla si es positivo, negativo o cero.

numero = int(input("Ingresa un número entero: "))

if numero > 0:
    print("El número es positivo")
elif numero < 0:
    print("El número es negativo")
else:
    print("El número es cero")
