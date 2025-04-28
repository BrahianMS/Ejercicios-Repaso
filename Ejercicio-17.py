# Contar cuántas veces aparece un nombre en la lista.

listnom = ["Pablo", "Ana", "Maria", "Jose", "John", "Carla", "Ana", "Maria", "Ana"]

buscnom = input("ingrese el nombre que busca: ")
cant = listnom.count(buscnom)
print(f"El nombre {buscnom} aparece {cant} veces.")