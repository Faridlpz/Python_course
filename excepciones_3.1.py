import math

def calcularaiz(num):
    if num<0:
        raise ValueError("El numero no puede ser negativo")
    else:
        return math.sqrt(num)

op1 = int(input("Introduce tu numero: "))

try:
    print(calcularaiz(op1))
except ValueError as errornegativo:
    print(errornegativo)

print("Programa Terminado!")