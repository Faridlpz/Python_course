from io import open

archivo_texto=open("archivo.txt","w")
frase="Estupendo dia para estudiar python \n el jueves"
archivo_texto.write(frase)

archivo_texto.close()