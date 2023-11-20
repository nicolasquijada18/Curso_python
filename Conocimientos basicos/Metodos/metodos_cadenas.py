
cadena = "Texto de la cadena"
cadena_numerica = "123456"

#Funciones (se aplican asi funcion(parametro))

#Funcion dir proporciona el alcance actual de un objeto en particular
#Proporciona una vista de los atributos y metodos disponibles de un objeto
dir = dir(cadena)
#print(dir)


#Contamos el largo de la cadena
cadena_len = len(cadena)
#print(cadena_len)



#Metodos (se aplican si o si a objetos objecto.metodo(parametro))


#Convertir texto a mayusculas
cadena_mayus = cadena.upper()
#print(cadena_mayus)


#Convertir texto a minusculas
cadena_minus = cadena.lower()
#print(cadena_minus)


#Convertir primera letra en mayuscula (todas las mayusculas del texto se volveran minuscula)
cadena_capitalize = "oLa Como Estas"
cadena_cap = cadena_capitalize.capitalize()
#print(cadena_cap)


#Buscar una cadena de texto especifica (Devuelve el indice en que se encuentra el texto y si no se encuentra devuelve -1)
cadena_find = cadena.find("x")
#print(cadena_find)


#Buscar cadena especifica (Devuelve el indice al igual que find pero esta devuelve una excepcion si no retorna nada)
cadena_index = cadena.index("x")
#print(cadena_index)
#cadena_index_error = cadena.index("ola")


#Si el texto es numerico devuelve true (tiene que ser numeros en formato string)
cadena_is_numeric = cadena_numerica.isnumeric()
#print(cadena_is_numeric)


#Si es alfanumerico devuelve true (solo puede contener letras de la A a la Z y no puede contener caracteres especiales)
cadena_prueba_alfanumerico = "abcdefg"
cadena_prueba_1 = cadena.isalpha()
#print(cadena_prueba_1)

cadena_prueba_2 = cadena_prueba_alfanumerico.isalpha()
#print(cadena_prueba_2)


#Buscar la cantidad de veces que esta un texto en una cadena
cadena_count = cadena.count("e")
#print(cadena_count)


#Verificamos si una cadena empieza con un texto especifico
cadena_startswith = cadena.startswith("Tex")
#print(cadena_startswith)


#Verificamos si una cadena termina con un texto especifico
cadena_endswith = cadena.endswith("ena")
#print(cadena_endswith)


#Remplaza un pedazo de la cadena por otro texto (si no encuentra coincidencias devuelve cadena anterior y si encuentra remplaza todas las coincidencias con el parametro dado)
cadena_replace = cadena.replace("Texto", "Hola")
#print(cadena_replace)


#Separar cadena de texto (devuelve una lista)
cadena_split = cadena.split(" ")
contador = len(cadena_split)
#print(cadena_split)
#print(contador)



 
