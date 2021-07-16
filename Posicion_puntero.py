from io import open

archivo_texto=open("archivo.txt","r")



#archivo_texto.seek(0)

archivo_texto.seek(len(archivo_texto.read())/2)
print(archivo_texto.read())