# Agregar un número en una posición específica.

lista = [1, 3, 5, 7, 9, 11, 13]
print("Lista actual:", lista)

num = int(input("Ingrese un número: "))
posic = int(input("Ingrese la posición en la que desea añadir el número: "))

lista.insert(posic, num)
print("Lista modificada:", lista)
