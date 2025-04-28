# Combinar dos listas de palabras.

list1 = ["casa", "carro", "nevera", "ropa", "mascotas"]
list2 = ["calle", "puente", "edificio", "parque"]
print("La primera lista es:", list1)
print("La segunda lista es:", list2)


comb = list1 + list2
print("Las listas combinadas son: ", comb)

# otra forma
list1.extend(list2)
print("La lista queda así:", list1)