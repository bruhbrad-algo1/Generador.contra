import random

longitud = int(input("Introduce la longitud de la contraseña: "))

contraseña = ""

simbolos = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

for i in range(longitud):
    contraseña += random.choice(simbolos)

print(f"Contraseña generada: {contraseña}")