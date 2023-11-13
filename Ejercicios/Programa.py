lista_numerica = [10, 15, 20, 30]
tupla_colores = ("rojo", "azul", "negro", "blanco")
conjunto_nombres = {"Juan", "Pedro", "Jaime", "Pepe"}
diccionario_colores = {
    "rojo" : 0,
    "azul" : 1,
    "negro" : 2,
    "blanco" : 3
}

nombre = "Juan"
color = "azul"
indice = int
valor = 0
puntos = int

if nombre in conjunto_nombres:
    if color in tupla_colores:
        if color == "blanco":
            indice = diccionario_colores["blanco"]        
        elif color == "negro":
            indice = diccionario_colores["negro"]
        elif color == "azul":
            indice = diccionario_colores["azul"]
        else:
            indice = diccionario_colores["rojo"] 
        puntos = lista_numerica[indice]    
    else:
        print("Tu color no esta")    
    print(f"Tu nombre es {nombre} , te asignaron el color  {color}  asi que tienes  {puntos}  puntos")


    
else:
    print("No estas en la lista")    
    