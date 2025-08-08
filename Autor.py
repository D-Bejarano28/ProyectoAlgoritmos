class Autor:
    def __init__(self,nombre,nacionalidad,obras):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.obras = obras

    def mostrar(self):
        print(f'Nombre: {self.nombre}')
        print(f'Nombre: {self.nacionalidad}')
        for obra in  self.obras:
            obra.mostrar()
            print('_______________________________________________________________________')
