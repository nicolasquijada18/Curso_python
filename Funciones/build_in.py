#Las funciones build_in son funciones que estan integradas de por si en Python

#Encontrando numero mayor de una lista
lista = {2,4,5,6,7}
numero_mas_alto = max(lista)
print(numero_mas_alto)

#Encontrando numero menor de una lista
numero_menor = min(lista)
print(numero_menor)

#Redondando numeros y definiendo numero de decimales
numero = round(1.4312,2)
print(numero)

#Retorna false si -> 0, vacio, False, ninguno
resultado_bool = bool(None)
print(resultado_bool)

#Retorna True si todos los valores son verdaderos
#Si hay algun dato que sea False retorna False
resultado_all = all(("2fafa", 23, {141,4242}))
print(resultado_all)

#Sumar todos los elementos de un iterable
sum = sum(lista)
print(sum)