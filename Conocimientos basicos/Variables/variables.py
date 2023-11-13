#Concatenar con fstrings variables con distinto tipo de dato
numero = 5

texto = f"El numero es {numero} concatenado."
print(texto)


#Operadores de pertenencia (in) (not in) (Funciona para buscar la pertenencia de un valor)

falso = "5" not in texto
true = "5" in texto
print(f"El numero 5 no esta en el texto?: {falso}")
print(f"El numero 5 esta en el texto?:  {true}")

#Recomendado utilizar snake case para declarar variables

variable_con_snake_case = "variable_con_snake_case"