diccionario = {
    "nombre": "juan",
    "edad" : 22,
    "sexo" : 'M',
    "gay?" : True
}


#Metodos
#Devuelve las keys de un diccionario (retorna dict_item)
claves = diccionario.keys()
#print(claves)


#Obtener el valor con una key (no lanza error)
valor = diccionario.get("nombre")
#print(valor)

#Esto devuelve un error al no encontrar la key
#valor = diccionario["noexisto"]
#print(valor)


#Eliminar todo del diccionario
diccionario.clear()
#print(diccionario)


#Eliminar elemento del diccionario
diccionario.pop("nombre")
#print(diccionario)


#Obtener diccionario iterable
diccionario_iterable = diccionario.items()
print(diccionario)
print(diccionario_iterable)