#Utilizando bucles for para iterar conjuntos, listas y tuplas
animales = ["perro", "loro", "cocodrilo", "gato"]
numeros = [10,40,50,60]
for animal in animales:
    print(animal)
    
#Como iterar dos listas al mismo tiempo
for animal,numero in zip(animales,numeros):
    print("Recorriendo lista 1: " + animal)
    print(f"Recorriendo lista 2: {numero}")
    
#Iterar en un rango de valores
#El primer parametro esta incluido pero el segundo no
for num in range(10,20):
    print(num)


#Recorrer lista obteniendo su indice
#El metodo enumerate devuelve tuplas a las cuales luego puedes acceder
for num in enumerate(numeros):
    print(f"Este es el indice: {num[0]}")
    print(f"Este es el valor: {num[1]}")
    
#Utilizando desempaquetado con enumerate
for i,num in enumerate(numeros):
    print(i)
    print(num)
    
#Agregando else al bucle for (siempre se ejecuta al finalizar el bucle)
for numero in numeros:
    print(numero)
else:
    print("No hay mas numeros")
    
    
#Como saltar una iteracion
frutas = ["manzana" , "uva", "naranja", "ciruela"]
for fruta in frutas:
    if fruta == "manzana":
        #continue hace que se salte a la siguiente iteracion
        continue
    print(fruta)
    
#Evitar que el bucle se siga ejecutando

for fruta in frutas:
    print(fruta)
    if fruta == "naranja":
        break


#Recorrer cadena de texto
cadena = "Hola Nico"
for letra in cadena:
    print(letra)

#bucle for en solo una linea de codigo
numeros = [10,15,20,25]
numeros_duplicados = [num*2 for num in numeros]
print(numeros_duplicados)