import pickle

class Vehiculos():
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):
        self.enmarcha=True

    def acelerar(self):
        self.acelera=True

    def frenar(self):
        self.frena=True

    def estado(self):
        print("Marca: ",self.marca,"\nModelo: ",self.modelo)

class furgoneta(Vehiculos):
    def carga(self,carga):
        self.carga =carga
        if(self.carga):
            return "Esta cargada"
        else:
            return "No esta cargada"

class Moto(Vehiculos):
    hcaballito=""
    def caballito(self):
        hcaballito="caballito"
    def estado(self):
        print("Marca: ",self.marca,"\nModelo: ",self.modelo,"\nCaballito: ",self.hcaballito)



coche1 = Vehiculos("Mazda","MX5")
coche2 = Vehiculos("GOLF","ZZ")
coche3 = Vehiculos("BMW","SS")

coches = [coche1,coche2,coche3]

ficher = open("loscoches","wb")

pickle.dump(coches, ficher)

ficher.close()

del(ficher)

fichero=open("loscoches","rb")

lista = pickle.load(fichero)

fichero.close()

for c in lista:
    print(c.estado())

print(lista)