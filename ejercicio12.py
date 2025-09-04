PRECIO_BARRA = 3.49
DESCUENTO = 0.6  # 60%

num_barras = int(input("Ingresa el número de barras vendidas que no son del día: "))

precio_descuento = PRECIO_BARRA * DESCUENTO
precio_final = (PRECIO_BARRA - precio_descuento) * num_barras

print(f"Precio habitual de una barra: {PRECIO_BARRA}€")
print(f"Descuento por no ser fresca: {precio_descuento}€")
print(f"Coste final total: {precio_final}€")
