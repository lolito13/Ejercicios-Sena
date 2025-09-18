# Ejercicio 11
nombre = input("Introduce el nombre del producto: ")
precio = float(input("Introduce el precio unitario: "))
unidades = int(input("Introduce el número de unidades: "))
coste_total = precio * unidades
print("{:s} {:09.2f} {:03d} {:011.2f}".format(nombre, precio, unidades, coste_total))