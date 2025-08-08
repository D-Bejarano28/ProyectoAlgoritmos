class Obra:
    def __init__(self,id,titulo,nombre_artista,
                 nacionalidad_artista,f_nacimiento,f_muerte,
                 tipo,ano_creacion,img):
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
        print(f'ID: {self.id}')
        print(f'Título: {self.titulo}')
        print(f'Artista: {self.nombre_artista}')
        print(f'Nacionalidad del Artista: {self.nacionalidad_artista}')
    
    def mostrar_detalles(self):
        print(f'Título: {self.titulo}')
        print(f'Artista: {self.nombre_artista}')
        print(f'Nacionalidad: {self.nacionalidad_artista}')
        print(f'Fecha de Nacimiento: {self.f_nacimiento}')
        print(f'Fecha de muerte: {self.f_muerte}')
        print(f'Tipo de obra: {self.tipo}')
        print(f'Año de creación: {self.ano_creacion}')
        print(f'URL imagen: {self.img}')