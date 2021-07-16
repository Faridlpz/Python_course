def polindromo(num):
    copy = num
    rev=0
    remainder = 0
    while(num>0):
        remainder = num % 10
        rev = (rev*10)+remainder
        num = num//10
    if copy == rev:
        return "Palindromo"
    else:
        return "No"
num = int(input("Ingrese un numero: "))
print(polindromo(num))








