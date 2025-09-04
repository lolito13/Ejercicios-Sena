n = int(input("Ingresa un número entero positivo: "))

if n > 0:
    suma = n * (n + 1) // 2  # // hace división entera
    print("La suma de los primeros", n, "enteros es:", suma)
else:
    print("Por favor ingresa un número positivo.")
