import requests

# La funcion get_deparmentos nos permitira almacenar los datos de la API correspondientes a los departamentos

def get_departamentos():
    URL = "https://collectionapi.metmuseum.org/public/collection/v1/departments"
    response = requests.get(URL)
    data = response.json()
    return data

# La funcion get_ids nos permitira obtener los IDs de las obras de arte por departamento

def get_ids(id):
    
    
    URL = "https://collectionapi.metmuseum.org/public/collection/v1/objects?departmentIds="+str(id)

    response = requests.get(URL)
    ids = response.json()
    ids_list = ids['objectIDs']
    return ids_list


# Esta funcion nos permitira obtener la informacion completa para cada obra de arte 

def obra_arte(id_department):

    ids_list = get_ids(id_department)

    lista_obras = []

    for id in ids_list[:20]:
        URL = "https://collectionapi.metmuseum.org/public/collection/v1/objects/"+str(id)
        response = requests.get(URL)
        obra = response.json()
        lista_obras.append(obra)
    return lista_obras
   



