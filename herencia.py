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

mimoto=Moto("Honda","CBR")
mifugoneta=furgoneta("jeep","4x4")
mimoto.caballito()
mimoto.estado()
mifugoneta.carga(True)
mifugoneta.arrancar()
mifugoneta.estado()