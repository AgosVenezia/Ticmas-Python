#Ejercicio 3: Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

nro = int(input("Ingrese un nro entero: "))
if nro % 2 == 0:
    print("El número es par")
    print("El número " + str(nro) + " es par")
else:
    print("El número es impar")
    print("El número " + str(nro) + " es impar")