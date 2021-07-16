import math
arr = [10, 40, 30, 50, 20]

res = sum(arr) / len(arr)
a=0
for i in arr:
   a+= (i-res)**2

print(math.sqrt(a/len(arr)))