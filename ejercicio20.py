# Ejercicio 20
fecha = input("Introduce tu fecha de nacimiento (dd/mm/aaaa): ")
partes = fecha.split("/")
dia, mes, año = partes[0], partes[1], partes[2]
print("Día:", dia, "Mes:", mes, "Año:", año)