a = True
b = False

#AND
print(a and a) #True and True = True
print(a and b) #True and False = False
print(b and b) #False and False = False

print((3<4) and (4<5)) #True and True = True
print((3<4) and (6<5)) #True and False = False

#OR
print(a or a) #True or True = True
print(a or b) #True or False = True
print(b or b) #False or False = False

#Negación NOT
resultado = a and a
print(resultado) #True and True = True
print(not resultado) #False

resultado2 = a and b
print(resultado2) #True and False = False
print(not resultado2) #True