#Problema dado por dalto 3
#Debo solicitar el nombre de los alumnos que asistieron a clase
#El alumno mayor es el profesor y el menor el asistente

#Debo registrar la edad de los alumnos, definir quien es asistente y quien profesor

quedan_alumnos = True
alumnos = []

while quedan_alumnos == True:
    nombre = input("Ingrese el nombre del alumno:\n")
    edad = int(input("Ingrese la edad del alumno:\n"))
    alumnos.append(tuple([nombre,edad]))
    
    s_n = input("Desea registrar otro alumno? (S/N):\n")
    
    if s_n.lower() == "n":
        quedan_alumnos = False
    elif s_n.lower() != "n" and s_n.lower() != "s":
       print("Respuesta invalida")
       break


def encontrarMinYMax(alumnos):
    alumno_mayor = max(alumnos, key= lambda x:x[1])
    alumno_menor = min(alumnos, key= lambda x:x[1])
    
    print(f"El alumno que sera profesor el dia de hoy es {alumno_mayor[0]} y el alumno asistente sera {alumno_menor[0]}")

encontrarMinYMax(alumnos)

