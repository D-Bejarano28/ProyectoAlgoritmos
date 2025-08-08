class Obra:
    # Representa una obra de arte con los detalles pedidos
    def __init__(self,id,titulo,nombre_artista,
                 nacionalidad_artista,f_nacimiento,f_muerte,
                 tipo,ano_creacion,img):
        # Inicializa un objeto de la clase Obra

        # Argumentos usados:
        # id (int): El numero identifcador de la obra
        # titulo (str): El título de la obra
        # nombre_artista (str): El nombre del artista que creó la obra
        # nacionalidad_artista (str): La nacionalidad del artista
        # f_nacimiento (str): La fecha de nacimiento del artista
        # f_muerte (str): La fecha de muerte del artista
        # tipo (str): El tipo de obra
        # ano_creacion (int): El año en que se creó la obra
        # img (str): La URL de la imagen de la obra
        self.id = id
        self.titulo = titulo 
        self.nombre_artista = nombre_artista
        self.nacionalidad_artista = nacionalidad_artista
        self.f_nacimiento = f_nacimiento
        self.f_muerte = f_muerte
        self.tipo = tipo
        self.ano_creacion = ano_creacion
        self.img = img

    def mostrar(self):
        # Imprime en la terminal un resumen de la obra, incluyendo ID, título, nombre y
        # nacionalidad del artista
        print(f'ID: {self.id}')
        print(f'Título: {self.titulo}')
        print(f'Artista: {self.nombre_artista}')
        print(f'Nacionalidad del Artista: {self.nacionalidad_artista}')
    
    def mostrar_detalles(self):
        # Imprime en la terminal todos los detalles de la obra, ademas de la fecha de nacimiento
        # y muerte del artista y su nacionalidad
        print(f'Título: {self.titulo}')
        print(f'Artista: {self.nombre_artista}')
        print(f'Nacionalidad: {self.nacionalidad_artista}')
        print(f'Fecha de Nacimiento: {self.f_nacimiento}')
        print(f'Fecha de muerte: {self.f_muerte}')
        print(f'Tipo de obra: {self.tipo}')
        print(f'Año de creación: {self.ano_creacion}')
        print(f'URL imagen: {self.img}')