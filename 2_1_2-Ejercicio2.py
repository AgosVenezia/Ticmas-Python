#Ejercicio 2: Escribir un programa que pida al usuario dos números y devuelva su división. Si el usuario no introduce números debe devolver un aviso de error y si el divisor es cero también.

nro_1= int(input("Ingrese el dividendo: "))
nro_2= int(input("Ingrese el divisor: "))
if nro_2 == 0:
    print("Error, no es posible dividir por 0")
else:
    print(nro_1/nro_2)