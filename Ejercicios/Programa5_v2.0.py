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
#Buscadores
#Este es el metodo para buscar libros que se llamara cuando se desee buscar un libro por su nombre
def buscarLibroNombre(libro_nombre=None): 
    if libro_nombre == None: 
        libro_nombre = input("Ingresa el nombre del libro que deseas buscar\n")
    libro_nombre_lower = libro_nombre.lower() 
    for libro in Libros: 
        if libro['Nombre'].lower() == libro_nombre_lower: 
            nombre, precio, categoria = libro.values() 
            print(f"Su libro es: {nombre}\nCuesta: {precio}\nEntra en la categoria de: {categoria}") 
            break 
    else:
        print("No se encontro el libro solicitado")
#Este metodo debe ser diferente ya que dentro de una categoria pueden haber multiples libros
def buscarLibroCategoria(libro_categoria=None):
    if libro_categoria == None:
        libro_categoria = input("Ingresa la categoría del libro que deseas buscar\n")
    libro_categoria_lower = libro_categoria.lower()
    encontrado = False
    for libro in Libros:
        if libro['Categoria'].lower() == libro_categoria_lower:
            if not encontrado:
                print("Libros encontrados:")
                print("--------------------------------------------")
                encontrado = True        
            nombre, precio, categoria = libro.values()
            print(f"Nombre del libro: {nombre}\nCuesta: {precio}\nEntra en la categoría de: {categoria}\n--------------------------------------------")         
    if not encontrado:
        print("No se encontraron libros en la categoría ingresada.")
#En este metodo se buscara un libro segun un rango de precio que el usuario ingresara
def buscarLibroPrecio(rango_min=None, rango_max=None):
    if rango_min==None or rango_max==None:
        rango_min= int(input("Ingrese valor minimo del rango de precio\n"))
        rango_max= int(input("Ingrese valor maximo del rango de precio\n")) 
    encontrado = False
    for libro in Libros:
        if libro['Precio'] >= rango_min and libro['Precio'] <= rango_max:
            if not encontrado:
                print("Libros encontrados:")
                print("--------------------------------------------")
                encontrado = True
            nombre, precio, categoria = libro.values()
            print(f"Nombre del libro: {nombre}\nCuesta: {precio}\nEntra en la categoría de: {categoria}\n--------------------------------------------")       
    if not encontrado:
        print("No se encontraron libros en el rango de precio ingresado")
parametro = input("Ingrese como desea buscar un libro (nombre, rango de precio o categoria)\n")
if parametro.lower() == "nombre":
    buscarLibroNombre()
if parametro.lower() == "precio":
    buscarLibroPrecio()
if parametro.lower() == "categoria":
    buscarLibroCategoria()
else:
    print("La opcion ingresada es incorrecta.")
#En esta version se logro reducir las lineas de codigo realizando lo mismo que se realizava en la version 1.0
#Esta version requiere upgrades en el metodo buscarLibroPrecio() y ademas validaciones
#Falta comentar el codigo
    
    

    

