# Programa que identifique si un número es primo
import math

print("PROGRAMA QUE DETERMINA SI UN NÚMERO ES PRIMO")
print("Ingresa el número")
numero = int(input())

esPrimo = True
i = 2
while i <= math.sqrt(numero):
    if numero % i == 0:
        esPrimo = False
    i += 1

if esPrimo:
    print("Sí es primo")
else:
    print("No es primo")
