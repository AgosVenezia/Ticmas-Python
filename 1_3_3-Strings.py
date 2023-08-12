#Operaciones con variables de tipo strings

cadena = "Layla"
texto_concatenado = cadena + ", Ingeniera en Sistemas de Información"
print(texto_concatenado) #Layla, Ingeniera en Sistemas de Información

print(cadena * 5) #LaylaLaylaLaylaLaylaLayla
#print(cadena / 5) #TypeError: unsupported operand type(s) for /: 'str' and 'int'

nombre = "Layla Scheli" #string

nombre_mayuscula = nombre.upper()
nombre_minuscula = nombre.lower()
print(nombre_mayuscula) #LAYLA SCHELI
print(nombre_minuscula) #layla scheli