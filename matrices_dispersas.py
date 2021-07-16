n = 10
queries = [[1,5,3],[4,8,7],[6,9,1]]

myList = [0] * (n+2)
suma =0
maxSum=0

for a,b,k in queries:
    myList[a]+=k
    myList[b+1]-=k
    

for i in myList:
    suma = suma+i
    maxSum = max(maxSum,suma)

print(maxSum)
    


