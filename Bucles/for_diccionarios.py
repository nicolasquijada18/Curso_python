#Creando diccionario

diccionario = dict(nombre="Lucas", apellido="dalto", edad=28, sexo="porfavor")



#Recorriendo diccionario obteniendo keys
for key in diccionario:
    print(key)
    
#Recorriendo diccionario obteniendo valor
for value in diccionario.values():
    print(value)
    
#Recorriendo diccionario obteniendo llave, valor
for key, value in diccionario.items():
    print(key)
    print(value)