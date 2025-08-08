class Autor:
    # Representa a un autor con su información personal y una lista de sus obras
    def __init__(self,nombre,nacionalidad,obras):
        #  Inicializa un objeto de la clase Autor

        # Argumentos usados:
        # nombre (str): El nombre del autor
        # nacionalidad (str): La nacionalidad del autor
        # obras (list): Es una lista de objetos de tipo Obra creados por el autor
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.obras = obras

    def mostrar(self):
        # Imprime en la terminal los detalles del autor como lo son su nombre, nacionalidad y sus obras
        print(f'Nombre: {self.nombre}')
        print(f'Nombre: {self.nacionalidad}')
        for obra in  self.obras:
            obra.mostrar()
            print('_______________________________________________________________________')
