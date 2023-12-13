#Creando conjunto con set()
conjunt = set(["dato 1" , "dato 2"])

#Metiendo conjunto dentro de otro conjunto
conjunto1 = {"affa", "afsaa"}
#conjunto2 = {"conjunto22141", conjunto1}#Asi no se puede hacer
#Se utiliza esta funcion frozenset()
conjunto3 = frozenset(["afa", "Afa"])
conjunto1 = {"fasf", "afsaf", conjunto3}
print(conjunto1)

#Teoria de conjuntos
#Identificando si es un subconjunto con issubset() y con <=
conjunto_a = {3,5,6,7}
subconjunto = {3,5,7}
es_subconjunto = subconjunto.issubset(conjunto_a)
es_subconjunto_a = subconjunto <= conjunto_a
#print(es_subconjunto_a)


#Identificando si es un supeconjunto con issuperset() y >=
conjunto_b = {3,6,7}
superconjunto = {3,5,6,8,7,9}
es_superconjunto = superconjunto.issuperset(conjunto_b)
es_superconjunto_b = superconjunto > conjunto_b
#print(es_superconjunto_b)


#Verificar si hay algun dato en comun. Devuelve false si hay elementos que coniciden
resutado = conjunto_b.isdisjoint(conjunto_a)
print(resutado)