# Pregunta si una persona terminó su tarea.
# Si no terminó, mostrar "Debes terminar la tarea".

term = input("Terminaste tu tarea? (si/no): ")

if term == "no":
    print("Debes terminar la tarea")
else:
    print("Bien hecho")