class Persona():
    def __init__(self,nombre,edad,lugar):
        self.nombre=nombre
        self.edad=edad
        self.lugar=lugar
    def descripcion(self):
        print("Nombre: ",self.nombre,"\nEdad",self.edad,"\nResidencia: ",self.lugar)

class Empleado(Persona):
    def __init__(self,salario,antiguedad,nombre_empleado,edad_empleado,lugar_empl):
        super().__init__(nombre_empleado,edad_empleado,lugar_empl)
        self.salario=salario
        self.antiguedad=antiguedad
    
    def descripcion(self):
        super().descripcion()
        print("salario: ",self.salario,"Antigueadad: ",self.antiguedad)


antonio=Empleado(1500,5,"farid",22,"gdl")
antonio.descripcion()