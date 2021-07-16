import math 


def Aimnumber(num):
    p =str(num)
    l = len(p)
    resultado =0
    for i in p:
        i = int(i)
        resultado += pow(i,l)
    if num == resultado:
        return "Yes"
    else:   
        return 'No'



print(Aimnumber(153))


    