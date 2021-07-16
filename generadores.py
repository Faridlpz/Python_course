def generar_pares(limite):
    num = 1
    while num < limite:

        yield num*2
        num = num+1

devuelve_pares = generar_pares(10)

print(next(devuelve_pares))
print("Aqui podria ir mas codigo...")
print(next(devuelve_pares))
print("Aqui podria ir mas codigo...")
print(next(devuelve_pares))