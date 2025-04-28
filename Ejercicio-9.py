# Pide una nota (0-10).
# Muestra si perdio, aprobado o sobresaliente.

nota = int(input("Ingrese la nota (1-10): "))

if nota >=0 and nota < 5:
    print("Perdiste")
elif nota >= 5 and nota < 7:
    print("Aprobaste")
elif nota >=7 and nota <= 10:
    print("Sobresaliente")
else:
    print("Nota inválida")