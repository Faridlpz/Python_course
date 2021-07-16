x1= 0
v1 = 2
x2 = 5
v2 = 3
aux=0

while (x1 <10000) or (x2>x1) or (x2<10000):
    x1 = x1 + v1
    x2 = x2 + v2
    aux=0
    if x1==x2:
    
        aux=1
        break

if aux==1:
    print("yes")
else:
    print("no")
    