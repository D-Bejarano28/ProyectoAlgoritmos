# Importammos los módulos de las clases y el modulo para el manejo de la api

from Departamento import Departamento
from Autor import Autor
from Obra import Obra
from api_management import *

class MetroArt:

    def __init__(self,db_departamentos,db_nacionalidades):
        self.db_departamentos = db_departamentos
        self.db_nacionalidades = db_nacionalidades

    def inicio(self):
        self.crear_departamentos()

        while True:

            print('''
                                -----BIENVENIDO A METROART-----
                     
                     Ingrese el numero correspondiente a al departamento que desea ver:

                     
            ''')
            self.mostrar_departamentos()
            
            opcion = input('\nOpcion de departamento: ')
            while not opcion.isnumeric() or int(opcion) not in range(1,22) or opcion == '2' or opcion == '20':
                opcion = input('NO EXISTE UN DEPARTAMENTO CON ESE ID!! Ingresa un numero que corresponda a un departamento: ')


            self.obras_info = obra_arte(int(opcion),0)
            # Creacion de todos los objetos obra y autores
            self.crear_obras()
            self.crear_autores()
            # Muestra de obras para el departamento seleccionado
            self.mostrar_obras()

            menu = input('''
            ¿Ahora que deseas hacer?
            1. Ver obras de un autor específico
            2. Ver obras por nacionalidad del artista
            3. Ver mas obras (Del mismo departemento)
            4. Salir del sistema
                         
            ---> Ingrese el número correspondiente a la opción que desea: 
            ''')
            while not menu.isnumeric() or int(menu) not in range(1,5):
                menu = input('Dato Inválido!! Ingrese un numero que corresponda a la opción que desea:  ')

            if menu == '1':
                self.mostrar_autores()
                if self.opcion_detalles():
                    obra = self.mostrar_detalles()   
            elif menu == '2':
                self.mostrar_obra_nacionalidad()
                if self.opcion_detalles():
                    obra = self.mostrar_detalles()
            elif menu == '3':
                pass     
            elif menu == '4':
                break



    def crear_departamentos(self):
        self.lista_departamentos = []
        departamento_info = self.db_departamentos['departments']
        for departamento in departamento_info:
            d_nuevo = Departamento(departamento['departmentId'],departamento['displayName'])
            self.lista_departamentos.append(d_nuevo)


    def crear_obras(self):
        self.lista_obras = []
        for obra in self.obras_info:
            if obra['artistDisplayName'] == '':
                nombre_artista = 'Anónimo'
            else:
                nombre_artista = obra['artistDisplayName']

            if obra['artistNationality'] == '':
                nacionalidad_artista = 'Desconocida'
            else:
                nacionalidad_artista = obra['artistNationality']
            o_nueva = Obra(obra['objectID'],obra['title'],nombre_artista,
                           nacionalidad_artista,obra['artistBeginDate'],obra['artistEndDate'],
                           obra['classification'],obra['objectBeginDate'],obra['primaryImage'])
            self.lista_obras.append(o_nueva)


    def crear_autores(self):
        self.lista_autores = []
        
        for autor in self.obras_info:
            lista_obras = []
            for obra in self.lista_obras:
                if obra.nombre_artista == autor['artistDisplayName']:
                    lista_obras.append(obra)

                if autor['artistDisplayName'] == '':
                    nombre_encontrado = 'Anónimo'
                else:
                    nombre_encontrado = autor['artistDisplayName']

                if autor['artistNationality'] == '':
                    nacionalidad = 'Anónimo'
                else:
                    nacionalidad = autor['artistNationality']

            a_nuevo = Autor(nombre_encontrado,nacionalidad,lista_obras)
            self.lista_autores.append(a_nuevo)


    def mostrar_departamentos(self):
        for departamento in self.lista_departamentos:
                print(f'{departamento.id} -- {departamento.nombre}')


    def mostrar_obras(self):
        for i in self.lista_obras:
                i.mostrar()
                print('_______________________________________________________________________')

    def mostrar_obra_nacionalidad(self):

        cont = 0
        
        for index,nacionalidad in enumerate(self.db_nacionalidades):
            print(f'{index} - {nacionalidad}')
            print()

        opcion_nacionalidad = input('Ingrese el numero  correspondiente a la nacionalidad del autor: ')
        while not opcion_nacionalidad.isnumeric() or int(opcion_nacionalidad) not in range(len(self.db_nacionalidades)+1):
            opcion_nacionalidad = input('Dato inválido!! Inngrese un numero que corresponda con una nacionalidad: ')

        nacionalidad_encontrada = self.db_nacionalidades[int(opcion_nacionalidad)]

        for obra in self.lista_obras:
            if obra.nacionalidad_artista == nacionalidad_encontrada:
                obra.mostrar()
                print('__________________________________________________________________________')
                cont += 1

        if cont == 0:
            print('No econtramos un artista con esa nacionalidad!')


    def mostrar_autores(self):
        lista_nombres_autor = []
        for autor in self.lista_autores:
            lista_nombres_autor.append(autor.nombre)
            set_muestra = set(lista_nombres_autor)
        for nombre in set_muestra:
            print()
            print(nombre)
        opcion_autor = input('Ingrese el nombre del autor deseado:')
        for autor in self.lista_autores:
            if autor.nombre == opcion_autor:
                vista_autor = autor
        if not vista_autor:
            print('Autor no encontrado!!!')

        print(vista_autor.nombre)
        for obra in vista_autor.obras:
            obra.mostrar()
            print('___________________________________________________________________________')


    def mostrar_detalles(self):
        cont = 0
        opcion_obra = input('Ingrese el id correspondeinte a la obra que desea detallar: ')

        while not opcion_obra.isnumeric():
            opcion_obra = input('El dato que ingresó no es válido!! Ingrese un id correspondiente a una obra: ')

        for obra in self.lista_obras:
            if int(opcion_obra) == obra.id:
                obra_encontrada = obra
                obra_encontrada.mostrar_detalles()
                cont += 1

        if cont == 1:
            return obra_encontrada
        else:
            print('No se encontró ninguna obra con ese id!!')
            

    def opcion_detalles(self):

        opcion = input('''
        Desea ver los detalles de la obra?
        1. Si
        2. No 
        ''')
        while not opcion.isnumeric() or int(opcion) not in range(1,3):
            opcion = input('Dato invalido!! Ingrese un numero correspondiente a la opcion: ')

        if opcion == '1':
            return True
        else:
            return False