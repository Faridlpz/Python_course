import pickle

class Persona:
    def __init__(self,nombre,genero,edad):
        self.nombre = nombre
        self.genero = genero 
        self.edad = edad
        print("Se ha creado una persona nueva con el nombre de: ",self.nombre) 

    def __str__(self):
        return "{} {} {}".format(self.nombre,self.genero,self.edad)

class ListaPersonas:
    lista = []

    def __init__(self):
        listadePersonas = open("fichero","ab+")
        listadePersonas.seek(0)
        try:
            self.lista=pickle.load(listadePersonas)
            print("Se gargaron {} personas del fichero externo. ".format(len(self.lista)))
        except:
            print("El fichero esta vacio")

        finally:
            listadePersonas.close()
            del(listadePersonas)

    def agregarPersonas(self,p):
        self.lista.append(p)
        self.guardarpersonas()

    def mostrarPersonas(self):
        for i in self.lista:
            print(i)

    def guardarpersonas(self):
        ListaPersonas=open("fichero","wb")
        pickle.dump(self.lista,ListaPersonas)
        ListaPersonas.close()
        del(ListaPersonas)

    def mostrarinfofichero(self):
        print("La informacion del fichero externo es: ")
        for p in self.lista:
            print(p)

miLista = ListaPersonas()
p = Persona("Sandra","Femenino","21")
miLista.agregarPersonas(p)
p = Persona("Farid","Masculino","24")
miLista.agregarPersonas(p)
p = Persona("Grecia","Femenino","12")
miLista.agregarPersonas(p)

miLista.mostrarinfofichero
