#Forma no optima de sumar valores de una lista

def suma(lista):
    numero_sumado = 0
    for numero in lista:
        numero_sumado = numero_sumado + numero
    return numero_sumado
    
resultado = suma([10,10,10])
print(resultado)
    
    
#Forma correcta de hacerlo (utilizando parametro args)
#Lo que hace args que toma todos los parametros entregados y los junta a un unico valor
def suma1(*numeros):
    return sum(numeros)

#No es necesario entregar como parametro una lista ya que el parametro args lo guarda como un iterable
resultado = suma1(10,40,50,20,40,20,40)
print(resultado)
