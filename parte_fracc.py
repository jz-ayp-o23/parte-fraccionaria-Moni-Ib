"""
Diseña un programa para determinar si un número tiene parte fraccionaria (decimales).
"""

# Declaraciones
CONSTANTE = 0

# Entradas
entrada = float(input("Introduzca un número: "))

# Proceso
if entrada % 1 == CONSTANTE :
    fraccionario = "No tiene decimales"

else:
    fraccionario = "Sí tiene deciamles"

# Salidas
print(fraccionario)
