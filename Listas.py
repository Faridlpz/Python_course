arr = [
    [1 ,1 ,1 ,0 ,0 ,0],
    [0 ,1 ,0 ,0 ,0 ,0],
    [1 ,1 ,1 ,0 ,0 ,0],
    [0 ,0 ,2 ,4 ,4 ,0],
    [0 ,0 ,0 ,2 ,0 ,0],
    [0 ,0 ,1 ,2 ,4 ,0]
]

suma=0
lista = []
for i in range(4):
    for j in range(4):
        suma = arr[i][j]+arr[i][j+1]+arr[i][j+2] + arr[i+1][j+1]
        +arr[i+2][j]+arr[i+2][j+1] +arr[i+2][j+2] 
        lista.append(suma)

print(max(lista))
       