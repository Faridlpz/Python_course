arr = [
     [10,20,30,40],
     [15,25,35,45],
     [27,29,37,48],
     [32,33,39,50]
]

x = 100
arreglo = []

for i in range(len(arr)):
    for j in range(len(arr)): 
        res = arr[i][j] == x
        if res == True:
            arreglo.append(i)
            arreglo.append(j)    
    
if not arreglo:
    print("Numero no encontrado")
else:
    print(arreglo)