class Departamento:
    def __init__(self,id,nombre):
        self.id = id
        self.nombre = nombre

    def mostrar(self):
        print(f'{self.id} - {self.nombre}')