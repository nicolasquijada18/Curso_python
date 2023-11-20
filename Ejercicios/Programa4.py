#Problema dalto 2
#Persona promedio habla 2 palabra por segundo
promedio = 2

#A)Pedirle al usuario que diga cualquier texto real y:
texto = input("Escribe cualquier texto real:\n")


#-Calcular cuanto tardaria en decir esa frase
contador = len(texto.split(" ")) 
tiempo = (contador*0.5)
print(f"Una persona promedio tardaria en decir este texto {tiempo} segundos.")

#-Cuantas palabras dijo?

print(f"El total de palabras que ingresaste por consola es: {contador} palabras.")

#B)Si se tarda mas de un minuto decirle: "Para flaco tampoco te pedi un testamento"
if tiempo > 60.0 :
    print("Para flaco tampoco te pedi un testamento")


#C)Dalto habla un 30% mas rapido que el promedio: Cuanto tardaria en decirlo?
tiempo_dalto = round(tiempo*0.3, 1)
print(f"Dalto tardaria {tiempo_dalto} segundos en decir ese texto.")
