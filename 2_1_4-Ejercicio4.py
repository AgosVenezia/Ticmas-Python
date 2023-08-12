#Ejercicio 4: Solicitar al usuario que ingrese dos números y mostrar cuál de los dos es menor. Considerar el caso en que ambos números son iguales.

nro_1= int(input("Ingrese un número: "))
nro_2= int(input("Ingrese otro número: "))
if nro_1 < nro_2:
    print("El primero es menor")
elif nro_2 < nro_1: #elif evalúa múltiples condiciones
    print("El segundo es menor")
else:
    print("Los números son iguales")