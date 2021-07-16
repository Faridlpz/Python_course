s = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]



def find_short(s):
    s = s.split() # splits the string into a list of individual words
    l = min(s, key = len) # finds the shortest string in the list
    return len(l) # returns shortest word length

print(find_short(s))