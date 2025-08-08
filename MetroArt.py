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
                pass    
            elif menu == '2':
                pass 
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

    
    def mostrar_departamentos(self):
        for departamento in self.lista_departamentos:
                print(f'{departamento.id} -- {departamento.nombre}')