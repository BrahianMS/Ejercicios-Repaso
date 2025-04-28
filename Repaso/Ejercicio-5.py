# Pide dos números.
# Si ambos son mayores que 0, muestra "Ambos son positivos".

num1 = float(input("Ingrese un número: "))
num2 = float(input("Ingrese otro número: "))

if num1 > 0 and num2 > 0:
    print("Ambos son positivos")
else:
    print("Al menos uno no es positivo")