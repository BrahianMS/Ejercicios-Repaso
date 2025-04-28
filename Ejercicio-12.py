# Dada una lista de frutas,
# pide al usuario una fruta que quiera eliminar.

listf = ["mango", "manzana", "arroz", "banano", "pera"]
print(listf)

frut = input("Qué fruta desea eliminar?: ")
if frut in listf:
    listf.remove(frut)
    print("La fruta se ha eliminado")
    print(listf)
else:
    print(f"{frut} no se encuentra en la lista")
