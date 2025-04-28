# Buscar si un número existe en una lista
# y encontrar su posición.

lista = [2, 4, 6, 8, 10, 12, 14, 16]

num = int(input("ingrese un número: "))

if num in lista:
    print(f"{num} está en la posición {lista.index(num)} de la lista")
else:
    print(f"{num} no está en la lista")