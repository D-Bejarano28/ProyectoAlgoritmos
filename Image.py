import requests
from PIL import Image
import io
# Código extraido del apéndice A 
def guardar_imagen_desde_url(url, nombre_archivo):

    try:
        # Se realiza la petición GET a la URL.
        response = requests.get(url, stream=True)
        # Lanza una excepción para códigos de estado de error (4xx o 5xx).
        response.raise_for_status()

        # Determina la extensión del archivo a partir del Content-Type.
        content_type = response.headers.get('Content-Type')
        extension = '.jpg' # Valor por defecto.
        if content_type:
            if 'image/png' in content_type:
                extension = '.png'
            elif 'image/jpeg' in content_type:
                extension = '.jpg'
            elif 'image/svg+xml' in content_type:
                extension = '.svg'
        
        # Se crea el nombre completo del archivo con su extensión.
        nombre_archivo_final = f"{nombre_archivo}{extension}"

        # Se guarda la imagen en el archivo local.
        with open(nombre_archivo_final, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        
        print(f"Imagen guardada exitosamente como '{nombre_archivo_final}'")

        # Abre y muestra la imagen descargada.
        img = Image.open(nombre_archivo_final)
        img.show()
        
        return nombre_archivo_final

    except requests.exceptions.RequestException as e:
        print(f"Error al hacer el request: {e}")
    except IOError as e:
        print(f"Error al escribir o abrir el archivo de imagen: {e}")
    
    return None