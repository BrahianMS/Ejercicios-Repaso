# Crea una lista vacía
# y permite al usuario añadir 3 nombres.


lista = []

for i in range(3):
    nom = input("Ingrese un nombre: ")
    lista.append(nom)

print("lista de nombres:", lista)