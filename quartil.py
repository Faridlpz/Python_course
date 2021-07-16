from typing import List


arr = [5,3,7,8,12,13,14,18,21]
#5,3,7,8,12,13,14,18,21
#9,5,7,1,3
#1,3,5,7


def median(List):
        lon = len(List)
        if lon % 2 == 0:
            median = (List[(lon//2)]+List[(lon//2-1)])/2
        else:
            median = List[(lon//2)]
        return int(median)

arr = sorted(arr)
middle = len(arr)//2
if len(arr)%2 ==0:
    L = arr[:middle]
    U = arr[middle:]
else:
    L = arr[:middle]
    U = arr[middle+1:]

print(median(arr[:middle]))
print(median(arr))
print(median(U))

