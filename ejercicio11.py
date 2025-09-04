deposito = float(input("Ingresa la cantidad depositada en la cuenta: "))
interes = 0.04  # 4% anual

# Calcular saldo para cada año
saldo_anio1 = round(deposito * (1 + interes), 2)
saldo_anio2 = round(saldo_anio1 * (1 + interes), 2)
saldo_anio3 = round(saldo_anio2 * (1 + interes), 2)

print(f"Saldo tras el primer año: {saldo_anio1}")
print(f"Saldo tras el segundo año: {saldo_anio2}")
print(f"Saldo tras el tercer año: {saldo_anio3}")
