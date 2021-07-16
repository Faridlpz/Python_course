def  devuelve_ciudades(*ciudades): #el asteristico significa que recivira un numero indeterminado de elementos
    for elemento in ciudades:
        #for subelemento in elemento:
        yield from elemento

ciudades_devueltas = devuelve_ciudades("Madrid","Barcelona","Bilbao","Valencia")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))