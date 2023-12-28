#Ejercicio dado por dalto
#Debo crear una funcion que reciba un valor como limite de un rango para luego extraer los numeros primos de ese rango

def encontrarNumerosPrimos():
    rango = int(input("Ingresa el valor maximo del rango: \n"))
    valores_primos = []
    
    for i in range(rango):
        valor = lambda x:x%x == 0
        valores_primos.append(valor(i))
    
    print(valores_primos)
    
encontrarNumerosPrimos()