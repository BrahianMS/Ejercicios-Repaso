# Pide la edad y clasifica:
# niño, adolescente, adulto, anciano.

edad = int(input("Ingrese edad: "))

if edad > 0 and edad < 12:
    print("Es un niño")
elif edad >= 12 and edad < 18:
    print("Es un adolescente")
elif edad >= 18 and edad < 60:
    print("Es un adulto")
elif edad > 60:
    print("Es un anciano")
else:
    print("Edad no válida")