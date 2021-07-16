n = 2

lista = [[] for _ in range(n)]
lastAnswer = 0
queries = [1,2,3]

for i,x,y in range(len(queries)):
    if i == 1:
        idx = ((x ^ lastAnswer) % n)
        lista[idx].append(y)
    else:
        idx = ((x ^ lastAnswer) % n)
        lastAnswer = lista[idx][y % len(lista[idx])]
        print(lastAnswer)
