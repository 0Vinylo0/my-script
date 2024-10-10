import os
import requests
import base64

# Configuraciones
TOKEN = ''  # Reemplaza con tu token
REPO = ''  # Reemplaza con tu usuario/repo
DIRECTORIO = ''  # Reemplaza con la ruta donde están tus archivos

# Función para obtener la lista de archivos en el repositorio
def obtener_archivos_repo():
    api_url = f'https://api.github.com/repos/{REPO}/contents/'
    response = requests.get(api_url, headers={'Authorization': f'token {TOKEN}'})
    
    if response.status_code == 200:
        return {item['path']: item['sha'] for item in response.json() if item['type'] == 'file'}
    return {}  # Devuelve un diccionario vacío si hay un error

# Función para obtener el SHA del archivo existente
def obtener_sha_archivo(ruta_repo):
    api_url = f'https://api.github.com/repos/{REPO}/contents/{ruta_repo}'
    response = requests.get(api_url, headers={'Authorization': f'token {TOKEN}'})
    
    if response.status_code == 200:
        return response.json()['sha']  # Retorna el SHA del archivo
    return None  # Si el archivo no existe

# Función para subir o actualizar el archivo
def subir_archivo(ruta_archivo, ruta_repo):
    sha = obtener_sha_archivo(ruta_repo)  # Obtener el SHA del archivo existente
    with open(ruta_archivo, 'rb') as f:
        contenido = f.read()
    contenido_encoded = base64.b64encode(contenido).decode()

    api_url = f'https://api.github.com/repos/{REPO}/contents/{ruta_repo}'

    if sha:
        # Actualiza el archivo existente
        data = {
            'message': 'Actualización automática del archivo',
            'content': contenido_encoded,
            'sha': sha
        }
    else:
        # Crea un nuevo archivo
        data = {
            'message': 'Subida automática del archivo',
            'content': contenido_encoded
        }

    # Realiza la solicitud PUT para subir el archivo
    response = requests.put(api_url, headers={'Authorization': f'token {TOKEN}'}, json=data)

    if response.status_code in [200, 201]:
        print(f"Archivo '{ruta_repo}' subido/actualizado exitosamente.")
    else:
        print(f"Error al subir '{ruta_repo}': {response.json()}")

# Función para eliminar archivos que ya no existen en el directorio local
def eliminar_archivos_faltantes(archivos_repo, directorio):
    # Obtiene todos los archivos del directorio local (incluidas subcarpetas)
    archivos_locales = set()
    for root, _, files in os.walk(directorio):
        for nombre_archivo in files:
            ruta_local = os.path.relpath(os.path.join(root, nombre_archivo), directorio)  # Ruta relativa
            archivos_locales.add(ruta_local)

    # Elimina los archivos del repositorio que no están en los archivos locales
    for nombre_archivo in archivos_repo.keys():
        if nombre_archivo not in archivos_locales:
            print(f"Eliminando archivo del repositorio: {nombre_archivo}")
            eliminar_archivo(nombre_archivo)

# Función para eliminar un archivo del repositorio
def eliminar_archivo(nombre_archivo):
    # Obtener el SHA del archivo a eliminar
    sha = obtener_sha_archivo(nombre_archivo)
    api_url = f'https://api.github.com/repos/{REPO}/contents/{nombre_archivo}'
    
    if sha:
        data = {
            'message': 'Eliminación automática del archivo',
            'sha': sha
        }
        response = requests.delete(api_url, headers={'Authorization': f'token {TOKEN}'}, json=data)
        if response.status_code == 204:
            print(f"Archivo '{nombre_archivo}' eliminado exitosamente.")
        else:
            print(f"Error al eliminar '{nombre_archivo}': {response.json()}")
    else:
        print(f"El archivo '{nombre_archivo}' no existe en el repositorio.")

# Recorre el directorio y sube los archivos
def sincronizar_archivos():
    # Obtener archivos actuales en el repositorio
    archivos_repo = obtener_archivos_repo()

    # Recorre el directorio y sube los archivos
    for root, _, files in os.walk(DIRECTORIO):
        for nombre_archivo in files:
            ruta_archivo = os.path.join(root, nombre_archivo)
            # Mantiene la estructura de carpetas
            ruta_repo = os.path.relpath(ruta_archivo, DIRECTORIO)  # Ruta relativa
            subir_archivo(ruta_archivo, ruta_repo)

    # Eliminar archivos que faltan
    eliminar_archivos_faltantes(archivos_repo, DIRECTORIO)

if __name__ == '__main__':
    sincronizar_archivos()
