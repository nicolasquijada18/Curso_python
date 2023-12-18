#Creando una funcion lambda
#Las funciones lambda son funciones anonimas que no requieren abrir bloques de codigo
multiplicar_x_2 = lambda x : x*2
print(multiplicar_x_2(2))

lista = [1,2,3,4,5,6]
#Usando filter con una funcion comun
def es_par(num):
    if(num%2==0): #Aqui preguntamos si el resto de la division del numero es igual a 0 significa que es par
         return True

numeros_pares = filter(es_par,lista)
print(list(numeros_pares))


#Lo mismo que antes pero con lambda
numeros_pares1 = filter(lambda numero:numero%2==0,lista)
print(list(numeros_pares1))