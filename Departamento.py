class Departamento:
    # Representa un departamento con un numero identificador y un nombre
    def __init__(self,id,nombre):
        # Inicializa un objeto de la clase Departamento

        # Args:
        # id (int): El identificador perteneciente al departamento
        # nombre (str): El nombre del departamento
        self.id = id
        self.nombre = nombre

    def mostrar(self):
        # Imprime en la consola el id y el nombre del departamento
        print(f'{self.id} - {self.nombre}')