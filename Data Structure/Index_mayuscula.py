def mayuscula(value):
    lista = []
    contador = 0
    for i in value:
        if i.isupper():
            lista.append(contador)
        contador = contador+1
    return lista





s = "HollAaa"

print(mayuscula(s))
