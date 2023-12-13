#Creando diccionario con dict()
diccionario = dict(nombre="lucas",apellido="dalto")
print(diccionario)
print(type(diccionario))

#Las listas no pueden ser claves porque son iterables, las tuplas si pueden ser claves
diiccionario_1 = {("alo", "hola"):"valor"}

#Creando un diccionario con valores none
#Este metodo itera el primer valor por lo tanto el primer parametro debe ser una lista
diccionario_2 = dict.fromkeys(["nombre", "apellido", "edad"])
print(diccionario_2)