# Programa que identifique si un número es primo
print("PROGRAMA QUE DETERMINA SI UN NÚMERO ES PRIMO")
print("Ingresa el número")
numero = int(input())

esPrimo = True
i = 2
while i < numero:
    if numero % i == 0:
        esPrimo = False
    i += 1

if esPrimo:
    print("Sí es primo")
else:
    print("No es primo")
