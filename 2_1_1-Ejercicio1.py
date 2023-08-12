#Ejercicio 1: Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

age = int(input("Ingrese su edad por favor: ")) #int convierte a entero un string
if age < 18:
    print("Eres menor de edad")
else:
    print("Eres mayor de edad")