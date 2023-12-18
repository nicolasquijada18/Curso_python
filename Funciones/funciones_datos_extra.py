#Asignando parametros en desorden
def frase(nombre,apellido,adjetivo):
    return f"Hola {nombre} {apellido}, eres muy {adjetivo}"
#Manera normal
#frase = frase("Nicolas", "Quijada", "vio")

#Manera desordenada (Keyword arguments)
frase = frase(nombre="Nicolas", adjetivo="rico", apellido="Quijada")
print(frase)


#Parametros predefinidos
def frase1(nombre,apellido,adjetivo="tonto"):
    return f"Hola {nombre} {apellido}, eres muy {adjetivo}"
fraseuno = frase1("Nicolas","Quijada")
print(fraseuno)
#Los parametros predefinidos se pueden modificar 
frase2 = frase1("Nicolas", "Quijada", "lindo")
print(frase2)