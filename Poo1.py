#Una clase contiene: estado, propiedades y comportamiento
class coche():
    def __init__(self): #Constructor de la clase 
        self.largochasis=250 # esto es una propiedad
        self.anchochasis=120
        self.__ruedas = 4 #El doble guion bajo hace que no pueda ser accesible a la variable
        self.enmarcha =False

    def arrancar(self,arrancamos):
        self.enmarcha=arrancamos

        
        if(self.enmarcha):
            chequeo=self.chequeo_interno()

        if(self.enmarcha and chequeo):
            return "El coche esta en marcha"

        elif(self.enmarcha and chequeo ==False):
            return "algo anda mal"
        else:
            return "el coche esta parado"


        
    def estado(self):
        print("El coche tiene",self.__ruedas, " Ruedas, un ancho de ",self.anchochasis)

    def chequeo_interno(self):
        print("Realizando chequeo interno")


        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"

        if(self.gasolina=="ok"and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False



micoche = coche()#Instancia
print(micoche.arrancar(True))
micoche.estado()


