#Problema dado por dalto
#Horas
minimo = 2.5
promedio = 4
maximo = 7
curso_dalto = 1.5
grabacion_cruda_otros = 5
#Se reduce en 4 
grabacion_cruda_dalto = 3.5
#Se reduce en una 1.5

#A) Diferencia en porcentaje entre el curso actual y:
#a.1-El mas rapido de otros cursos
#a.2-El mas lento de otros cursos
#a.3-El promedio de los cursos

#a.1)
porcentaje_curso_rapido = (100*1.5/2.5)
modulo1 = int(100-porcentaje_curso_rapido)



a_1 = f"El porcentaje de diferencia entre el curso de dalto y el mas rapido es de {modulo1}%"


#a.2)
porcentaje_curso_lento = (100*1.5/7)
modulo2 = int(100-porcentaje_curso_lento)

a_2 = f"El porcentaje de diferencia entre el curso de dalto y el mas lento es de {modulo2}%"


#a.3)
porcentaje_curso_promedio = (100*1.5/4)
modulo3 = int(100-porcentaje_curso_promedio)

a_2 = f"El porcentaje de diferencia entre el curso de dalto y el promedio es de {modulo3}%"


#B)Porcentaje del material inservible que se reduce en:
#-El promedio de los cursos
#-El curso actual(este curso)

#b.1)
porcentaje_b1 = int(100-(promedio*100/grabacion_cruda_otros))
b_1 = f"El porcentaje de material inservible que se reduce en otros cursos es de {porcentaje_b1}%"



#b.2)
porcentaje_b2 = int(100-(curso_dalto*100/grabacion_cruda_dalto))
b_2 = f"El porcentaje de material inservible que se reduce en el curso de dalto es de {porcentaje_b2}%"


#C)Ver 10 horas de este curso a cuantas de otros cursos equivale.
#Ver 10 horas de otros cursos a cuantas horas de este curso equivale

#c.1)
#???????????????????????????????????????????????????????
porcentaje_c1 = promedio/curso_dalto
