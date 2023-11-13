#Lista
modales = ["hola", "adios", "gracias", "denada"]

#Tupla
colores = ("rojo", "azul", "verde" , "amarillo")

#Conjunto
nombres = {"Maria", "Yankee", "Pedro", "Juan"}

#Diccionario
valores = {
    'nivel1' : 100,
    'nivel2' : 200,
    'nivel3' : 300
}

print(nombres)
print(modales)
print(colores)
print(valores)


#Acceder a dato especifico de la lista
print(modales[0])

#Acceder a dato especifico de tupla
print(colores[0])

#Acceder a dato especifico de conjunto
print(nombres[0])
#No se puede acceder al indice de un conjunto

#Acceder a dato especifico de diccionario
print(valores['nivel1'])

#Modificar dato lista
modales[3] = "Cuidate"

#Modificar dato tupla
colores[3] = "Negro"
#Las tuplas no se pueden modificar





#Las listas se pueden modificar accediendo al indice pero, las tuplas no.
#En los conjuntos no pueden haber datos duplicados y tampoco se pueden modificar accediendo a indice

