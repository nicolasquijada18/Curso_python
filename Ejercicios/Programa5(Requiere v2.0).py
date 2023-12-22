#Buscador de libros, buscara segun precio, segun categoria y por nombre.
#Lista con diccionarios de libros
Libros = [{
    'Nombre' : "Don quijote",
    'Precio' : 5000,
    'Categoria' : "Aventura"
    },
    {
       'Nombre' : "Principe de persia",
       'Precio' : 8000,
       'Categoria' : "Aventura"
    },
    {
        'Nombre' : "Chavo del 8",
        'Precio' : 4000,
        'Categoria' : "Comedia"
    },
    {
        'Nombre' : "Padre rico padre pobre",
        'Precio' : 10000,
        'Categoria' : "Finanzas"
    }]
#Buscador
print("Bienvenido al buscador de libros version 1.0, aqui podras buscar libros segun su categoria, precio y por su nombre")
#Respuesta del usuario para saber que desea buscar
respuesta_1 = input("Ingresa como deseas buscar el libro (Precio, Categoria, Nombre)\n")
#If para validar si ingreso opcion correcta
if (respuesta_1 != "Precio" and respuesta_1 != "Categoria" and respuesta_1 != "Nombre"):
    print("Ingresaste una opcion incorrecta") 
elif respuesta_1 == "Categoria":
    lista_cat = []
    cat = input("Ingrese la categoria la cual quiere buscar\n")  
    #If para identificar que categoria desea buscar el usuario
    if cat != Libros[0]['Categoria'] and cat != Libros[1]['Categoria'] and cat != Libros[2]['Categoria'] and cat != Libros[3]['Categoria']:
        print("La categoria que ingresaste no existe")  
        exit()  
    #Ingresando a lista categoria los libros correspondientes    
    if cat == Libros[0]['Categoria']:
        lista_cat.append(Libros[0])
    if cat == Libros [1]['Categoria']:
        lista_cat.append(Libros[1])
    if cat == Libros[2]['Categoria']:
        lista_cat.append(Libros[2])
    if cat == Libros[3]['Categoria']:  
        lista_cat.append(Libros[3])
    print("Estos son los libros de la categoria que ingresaste\n")
    print("----------------------------------------------------\n") 
    print(lista_cat)
elif respuesta_1 == "Nombre":
    #Input que recoje el nombre del libro que busca el usuario
    nombre = input("Ingrese el nombre del libro que busca para mostrar sus datos: \n")
    #Si el nombre del libro no se encuentra en la lista libros sale del programa
    if nombre != Libros[0]['Nombre'] and nombre != Libros[1]['Nombre'] and nombre != Libros[2]['Nombre'] and nombre != Libros[3]['Nombre']:
        print("No se encontro el libro que ingresaste.")
        exit()
    #Comparando el nombre ingresado por los nombres de la lista Libros
    if nombre == Libros[0]['Nombre']:
        print("Informacion del libro: " + nombre)
        print(Libros[0])
    if nombre == Libros[1]['Nombre']:
        print("Informacion del libro: " + nombre)
        print(Libros[1])
    if nombre == Libros[2]['Nombre']:
        print("Informacion del libro: " + nombre)
        print(Libros[2])
    if nombre == Libros[3]['Nombre']:
        print("Informacion del libro: " + nombre)
        print(Libros[3])
    #Si el usuario ingresa precio entra a este elif
elif respuesta_1 == 'Precio':
    #Creo una tupla que almacena el valor minimo y maximo del rango  de precio
    rango_precio = ()
    rango_1 = int(input("Ingrese el valor minimo del precio de su libro: \n"))
    rango_2 = int(input("Ingrese el valor maximo del precio de su libro: \n"))
    #Condiciones para validar el rango ingresado
    if rango_1 > rango_2:
        print("El valor minimo no puede ser mas alto que el valor maximo.")
        exit()
    elif rango_1 == rango_2:
        print("El valor minimo y el valor maximo no pueden ser iguales.")    
        exit()
    elif rango_1 < 0 or rango_2 < 0:
        print("Los valores no pueden ser negativos")
        exit()
    rango_precio = (rango_1, rango_2)
    #Lista que almacena libros dentro del rango de precio
    lista_precios = []
    #Estos if evaluan si algun libro esta dentro del valor minimo y maximo ingresado
    if Libros[0]['Precio'] >= rango_precio[0] and Libros[0]['Precio'] <= rango_precio[1]:
        lista_precios.append(Libros[0])
    if Libros[1]['Precio'] >= rango_precio[0] and Libros[1]['Precio'] <= rango_precio[1]:
        lista_precios.append(Libros[0])
    if Libros[2]['Precio'] >= rango_precio[0] and Libros[2]['Precio'] <= rango_precio[1]:
        lista_precios.append(Libros[0])
    if Libros[3]['Precio'] >= rango_precio[0] and Libros[3]['Precio'] <= rango_precio[1]:
        lista_precios.append(Libros[3])
    if len(lista_precios) == 0:
        print("No hay ningun libro dentro del rango de precio que ingresaste :c")
    print("Estos son los libros dentro del rango de precio que ingresaste\n")
    print("---------------------------------------------------------------")
    print(lista_precios)
                
