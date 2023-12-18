#Se utiliza def para indicar que crearemos una nueva funcion
def saludar():
    print("Hola como estas rey, my king, rey de reyes")

#Ejecutando
saludar()

#Creando una funcion con parametro
def saludacion(nombre):
    print(f"Hola {nombre}, como estas?")
    
saludacion("Campeon")

#Creando funcion que retorna valores
def calculo(num):
    num_entero = str(num)
    return num_entero
 
dato = calculo(29)
print(dato)

    