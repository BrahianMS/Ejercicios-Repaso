# Pide la hora.
# Si es menor que 12 o mayor que 18, muestra "No es hora de trabajar".

hor = int(input("ingrese la hora: "))

if hor < 12 or hor > 18:
    print("No es hora de trabajar")
else:
    print("A trabajar")