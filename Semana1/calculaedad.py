fecha_nacimiento = input("Introduce tu fecha de nacimiento (dd/mm/aaaa): ")
dia, mes, anio = fecha_nacimiento.split('/')

edad = (2023 - int(anio)) - ((4, 27) < (int(mes), int(dia)))

print("Tu edad es:", edad, "años")
