values = [10, 40, 30, 50, 20, 10, 40, 30, 50, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20 ,10 ,40 ,30 ,50 ,20 ,10 ,40 ,30 ,50]
freqs = [1 ,2 ,3 ,4 ,5 ,6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7 ,8, 9, 10, 10, 40, 30, 50, 20, 10, 40, 30, 50, 20]
s = []

for i in range(len(values)):
    r = freqs[i]
    for e in range(r):
        s.append(values[i])
        
def median(List):
        lon = len(List)
        if lon % 2 == 0:
            median = (List[(lon//2)]+List[(lon//2-1)])/2
        else:
            median = List[(lon//2)]
        return median


s = sorted(s)
middle = len(s)//2
if len(s)%2 ==0:
    L = s[:middle]
    U = s[middle:]
else:
    L = s[:middle]
    U = s[middle+1:]

Q1=median(L)
Q3=median(U)

print(Q3-Q1)

    
    
    