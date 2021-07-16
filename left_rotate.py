arr = [1,2,3,4,5]
d=5


for i in range(1,d):
    arr+= [arr.pop(0)]
    

print(arr)