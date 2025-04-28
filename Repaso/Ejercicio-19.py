# Pide 5 números
# y crea una lista solo con los pares.

listpar = []

print("A continuación se le solicitarán cinco números")

for i in range(5):
    num = int(input("Ingrese el número: "))
    if num % 2 == 0:
        listpar.append(num)
if listpar == []:
    print("No ingresó ningún par")
else:
    print("La lista con los pares es: ", listpar)