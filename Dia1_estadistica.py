X=[10 ,40 ,30 ,50 ,20 ,10 ,40 ,30 ,50 ,20]
W=[1,2,3,4,5,6,7,8,9,10]
R = []
p = 0
p1 = 0
for i in range(len(X)):
    R.append(X[i] * W[i])
    p = sum(R)
    p1 =sum(W)

p1 = p/p1

print(round(p1,1))