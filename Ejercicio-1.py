# Un usuario ingresa una contraseña.
# Verifica si la contraseña es igual a "1234".


passw = str(input("ingrese contraseña: "))

if passw == "1234":
    print("Acceso permitido")
else:
    print("Acceso denegado")