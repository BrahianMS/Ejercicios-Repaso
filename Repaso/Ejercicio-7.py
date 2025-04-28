# Pregunta si una persona tiene licencia y si lleva casco.
# Si no tiene licencia o no lleva casco, no puede conducir.

lic = input("Tiene licencia? (si/no): ")
casc = input("Tiene casco? (si/no): ")

if lic != "si" or casc != "si":
    print("No puede conducir")
else:
    print("Puede conducir")