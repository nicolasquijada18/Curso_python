lista = ["hola", "adios", "gracias", "denada"]
lista_numerica = [3, 1, 8, 9, 5]
lista_vocales = ["a", "x" , "z", "i"]

#Funciones (se aplican asi funcion(parametro))

#Crear una lista (como parametro se le puede entregar una lista)
lista_list = list
#print(lista_list)

lista_list_2 = list(["lista", "numero", "dos"])
#print(lista_list_2)


#Cantidad de objetos de la lista
lista_len = len(lista)
#print(lista_len)


#Metodos (se aplican si o si a objetos objecto.metodo(parametro))

#Agregar un elemento a la lista
lista.append("buenas noches")
#print(lista)


#Agregar un elemento a la lista con un indice especifico
lista.insert(2, "provecho")
#print(lista)


#Agregar elementos a la lista (no se puede agregar uno tiene que ser una lista)
lista.extend(["anticucho", "ke personajes"])
#print(lista)


#Elimina un elemento de la lista por su indice
lista.pop(6)
lista.pop(6)
#Aqui es dos veces el indice 6 porque al eliminar un elemento el que era indice 6 pasa a ser indice 6 por la eliminacion del anterior
#print(lista)

#Elimnar ultimo elemento de la lista
#lista.pop(-1)


#Eliminar elemento de la lista por su valor
lista.remove("denada")
#print(lista)


#Eliminar todos los elementos de la lista
#lista.clear()
#print(lista)


#Ordenar lista de forma ascendente (No funciona con listas que tienen cadenas de texto)
lista_numerica.sort()
#print(lista_numerica)


#Ordenar lista de forma descendente
lista.sort(reverse=True)
#cprint(lista)

lista_vocales.sort()
#print(lista_vocales)


#Revertir lista
#print(lista)
lista.reverse()
#print(lista)


#Encontrar el indice en el que se encuentra un valor
indice_lista = lista.index("buenas noches")
#print(indice_lista)






