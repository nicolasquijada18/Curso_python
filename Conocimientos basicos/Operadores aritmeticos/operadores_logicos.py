#OR AND y NOT
#En este caso true y false representan si se cumplio alguna condicion.


#AND

R1 = True & True #Esto es true
R2 = True & False #Esto es falso
R3 = False & True #Esto es falso
R4 = False & False #Esto es falso
#Practicamente sirve para comprbar si se cumplen todas las condiciones.

#OR

R5 = True | True #Esto es true
R6 = False | True #Esto es true
R7 = True | False #Esto es true
R8 = False | False #Esto es falso
#Sirve para comprobar si alguna de las condiciones se cumple.

#NOT
R9 = not True #Devuelve falso
R10 = not False #Devuelve true
#Sirve practicamente para invertir la respuesta

R11 = not 3==3 #Devuelve falso
R12 = not 3 != 3 #Devuelve verdadero
