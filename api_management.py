import requests

<<<<<<< HEAD
# La funcion get_departamentos nos permitira almacenar los datos de la API correspondientes a los departamentos
# Estos datos corresponden a los IDs y nombres de departamentos
=======
# La funcion get_deparmentos nos permitira almacenar los datos de la API correspondientes a los departamentos
>>>>>>> 198ebe553b0ea143a8eeb7296877016dc88bc5f5

def get_departamentos():
    URL = "https://collectionapi.metmuseum.org/public/collection/v1/departments"
    response = requests.get(URL)
    data = response.json()
    return data

# La funcion get_ids nos permitira obtener los IDs de las obras. Retorna una lisra contodos los IDs de las obras por departamento

def get_ids(id):
    
    
    URL = "https://collectionapi.metmuseum.org/public/collection/v1/objects?departmentIds="+str(id)

    response = requests.get(URL)
    ids = response.json()
    ids_list = ids['objectIDs']
    return ids_list


<<<<<<< HEAD
# Esta funcion nos permitira obtener la informacion completa para cada obra de arte.
# Almacenará cada obra de arte en una lista.
=======
# Esta funcion nos permitira obtener la informacion completa para cada obra de arte 
>>>>>>> 198ebe553b0ea143a8eeb7296877016dc88bc5f5

def obra_arte(id_department,param):

    #LLamamos a la funcion para obtener los ids

    ids_list = get_ids(id_department)

    lista_obras = [] # Creamos la lista donde se almacenaran las obras
    primer_index = param # Estos indices nos permitiran ir obteniendo informacion de las obras por segmento
    ultimo_index = param + 20

    for id in ids_list[primer_index:ultimo_index]:
        # Al URL se le concatena un id para obtener la informacion de la obra que luego se agregará a la lista
        URL = "https://collectionapi.metmuseum.org/public/collection/v1/objects/"+str(id)
        try:

            response = requests.get(URL)
            response.raise_for_status()
            obra = response.json()
            if obra:
                lista_obras.append(obra)
        except requests.exceptions.RequestException:
            continue
    return lista_obras
   



