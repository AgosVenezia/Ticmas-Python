# Definir los sueldos de Juan por mes
sueldos_por_mes = [300, 300, 300, 300, 300, 300, 500, 500, 500, 500, 700, 700]

# Calcular el sueldo total y el sueldo promedio
sueldo_total = sum(sueldos_por_mes)
sueldo_promedio = sueldo_total / len(sueldos_por_mes)
sueldo_promedio = round(sueldo_promedio, 2) # Redondear a dos decimales

# Determinar la categoría del sueldo
if sueldo_promedio < 300:
    categoria = "Sueldo bajo"
elif sueldo_promedio <= 900:
    categoria = "Sueldo normal"
else:
    categoria = "Sueldo mejor de lo normal"

# Mostrar resultados en dos líneas de texto
print(f"El sueldo promedio de Juan es: {sueldo_promedio} dólares.")
print(f"Categoría de sueldo: {categoria}.")

# Mostrar resultados en una línea de texto
print(f"El sueldo promedio de Juan es: {sueldo_promedio} dólares y se encuentra dentro de la categoría {categoria}.")