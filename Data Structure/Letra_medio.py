def mid(value):
    if len(s)%2== 0:
        mid = ""
    else:
        mid = len(s)//2 
        mid = value[mid]
    return mid


s = 'abc'



print(mid(s))