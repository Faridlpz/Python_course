def solution(numero):
    suma=0
    for i in range(numero-1,0,-1):
        if (i % 3) == 0 or (i % 5 == 0):
            suma = suma + i
    return suma


numero = 10

print(solution(numero))

