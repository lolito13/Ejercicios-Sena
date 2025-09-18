# Ejercicio 21
productos = input("Introduce productos separados por comas: ")
for producto in productos.split(","):
    print(producto.strip())