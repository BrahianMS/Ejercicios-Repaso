# Un programa pide la edad de una persona.
# Si es mayor de 18, puede votar.

ed = int(input("ingrese edad"))

if ed >= 18:
    print("puedes votar")
else:
    print("no puedes votar")