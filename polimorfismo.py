class Coche():

    def desplazamiento(self):
        print("En cuatro ruedas")


class Moto():
    def desplazamiento(self):
        print("en dos ruedas")

class Camion():
    def desplazamiento(self):
        print("en seis ruedas")

def desplazamientovehiculo(vehiculo):
    vehiculo.desplazamiento()

mivehiculo=Camion()

desplazamientovehiculo(mivehiculo)