PESO_PAYASO = 112
PESO_MUNECA = 75

num_payasos = int(input("Ingresa el número de payasos vendidos: "))
num_munecas = int(input("Ingresa el número de muñecas vendidas: "))

peso_total = (num_payasos * PESO_PAYASO) + (num_munecas * PESO_MUNECA)

print(f"El peso total del paquete es {peso_total} gramos.")
