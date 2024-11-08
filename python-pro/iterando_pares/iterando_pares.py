import os
import re
import subprocess
import time
import json
import signal
import requests
from urllib.parse import urljoin

# Diccionarios para almacenar las URLs y sus IDs
urls_description = {}
urls_contiene = {}
# Archivos para mantener registro de las páginas procesadas y los resultados
processed_pages_file = "processed_pages.txt"
description_file = "description.json"
contiene_file = "contiene.json"
unprocessed_pages_file = "unprocessed_pages.txt"
log_file = "curl_log.txt"
# Cookie file para curl
cookie_file = "cookies.txt"

# Variable para detener el proceso de manera segura
global_stop = False

# Set para almacenar URLs en el ciclo actual
currently_processing = set()

def signal_handler(sig, frame):
    global global_stop
    global_stop = True
    print("\nProceso detenido por el usuario. Guardando progreso sin procesar la última URL...")
    # Asegurarse de que la última URL no sea eliminada de no procesadas
    if currently_processing:
        last_url = currently_processing.pop()
        save_unprocessed_page(last_url)

# Registrar la señal de interrupción (Ctrl+C)
signal.signal(signal.SIGINT, signal_handler)

# Crear archivos y directorios si no existen
for file in [cookie_file, processed_pages_file, log_file, description_file, contiene_file, unprocessed_pages_file]:
    if not os.path.exists(file):
        open(file, 'w').close()

# Función para leer las URLs ya procesadas
def load_processed_pages():
    if os.path.exists(processed_pages_file):
        with open(processed_pages_file, "r") as f:
            return set(f.read().splitlines())
    return set()

# Función para guardar las URLs procesadas
def save_processed_page(url):
    with open(processed_pages_file, "a") as f:
        f.write(url + "\n")

# Función para leer las URLs no procesadas
def load_unprocessed_pages():
    if os.path.exists(unprocessed_pages_file):
        with open(unprocessed_pages_file, "r") as f:
            return set(f.read().splitlines())
    return set()

# Función para guardar las URLs no procesadas
def save_unprocessed_page(url):
    with open(unprocessed_pages_file, "a") as f:
        f.write(url + "\n")

# Función para eliminar una URL del archivo de no procesadas
def remove_unprocessed_page(url):
    unprocessed_pages = load_unprocessed_pages()
    if url in unprocessed_pages:
        unprocessed_pages.remove(url)
        with open(unprocessed_pages_file, "w") as f:
            f.writelines([page + "\n" for page in unprocessed_pages])

# Cargar las páginas ya procesadas
processed_pages = load_processed_pages()
# Cargar las páginas no procesadas
unprocessed_pages = load_unprocessed_pages()

# Cargar los diccionarios description y contiene si existen
def load_json_data(filename):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}

urls_description = load_json_data(description_file)
urls_contiene = load_json_data(contiene_file)

# Función para realizar la solicitud curl y obtener el contenido HTML
def curl_request(url, is_contiene=False):
    try:
        if is_contiene:
            # Realizar una solicitud curl para obtener las cookies primero
            get_cookie_command = [
                "curl",
                "-sL",
                "-c", cookie_file,
                url
            ]
            subprocess.run(get_cookie_command, capture_output=True, text=True)

            # Luego hacer el curl con la cookie obtenida
            command = [
                "curl",
                "-sL",
                "https://pares.mcu.es/ParesBusquedas20/catalogo/contiene/SearchController.do",
                "-H", "Accept: text/html, */*; q=0.01",
                "-H", "Accept-Language: es-ES,es;q=0.9,en;q=0.8",
                "-H", "Connection: keep-alive",
                "-H", "Content-Type: application/x-www-form-urlencoded; charset=UTF-8",
                "-H", f"Cookie: {get_cookies()}",
                "-H", "Origin: https://pares.mcu.es",
                "-H", f"Referer: {url}",
                "-H", "Sec-Fetch-Dest: empty",
                "-H", "Sec-Fetch-Mode: cors",
                "-H", "Sec-Fetch-Site: same-origin",
                "-H", "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
                "-H", "X-Requested-With: XMLHttpRequest",
                "-H", "sec-ch-ua: \"Chromium\";v=\"130\", \"Google Chrome\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
                "-H", "sec-ch-ua-mobile: ?0",
                "-H", "sec-ch-ua-platform: \"Windows\"",
                "--data-raw", "tambloque=10000&orderBy=0"
            ]
        else:
            command = [
                "curl",
                "-sL",
                url
            ]
        result = subprocess.run(command, capture_output=True, text=True)
        # Guardar en el archivo de log
        with open(log_file, "a") as log:
            log.write(f"URL: {url}\nReturn Code: {result.returncode}\nOutput Length: {len(result.stdout)}\nOutput Preview: {result.stdout[:500]}\n\n")
        return result.stdout
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        with open(log_file, "a") as log:
            log.write(f"Error fetching {url}: {e}\n")
        return ""

# Función para obtener las cookies del archivo cookie_file
def get_cookies():
    cookies = []
    if os.path.exists(cookie_file):
        with open(cookie_file, "r") as f:
            for line in f:
                if not line.startswith("#") and line.strip():
                    parts = line.strip().split("\t")
                    if len(parts) >= 7:
                        cookies.append(f"{parts[5]}={parts[6]}")
    return "; ".join(cookies)

# Función principal para explorar enlaces recursivamente
def explore_links(url):
    global global_stop
    if global_stop:
        print("Exploración detenida antes de procesar la URL actual.")
        return

    if url in currently_processing:
        print(f"Detectado ciclo con la URL: {url}. Saltando a la siguiente URL no procesada.")
        next_link = get_next_unprocessed_link()
        if next_link:
            explore_links(next_link)
        return

    currently_processing.add(url)

    if url in processed_pages:
        print(f"URL ya procesada, pero se volverá a procesar: {url}")
        processed_pages.remove(url)  # Eliminar la URL para que no esté duplicada

    is_contiene = "contiene/" in url
    print(f"Explorando: {url}")
    html_content = curl_request(url, is_contiene=is_contiene)
    if not html_content:
        print(f"No se pudo obtener contenido de: {url}")
        next_link = get_next_unprocessed_link()
        if next_link:
            explore_links(next_link)
        return

    # Extraer ID y guardar en el diccionario adecuado
    if "description/" in url:
        match = re.search(r'description/(\d+)', url)
        if match:
            page_id = match.group(1)
            has_image = bool(re.search(r'href=["\'].*?show/.*?["\']', html_content))
            title_match = re.search(r'<h4[^>]*>Titulo Nombre Atribuido:</h4>\s*<p>(.*?)</p>', html_content, re.DOTALL)
            title = title_match.group(1).strip() if title_match else ""
            urls_description[page_id] = {
                "title": title,
                "url": url,
                "has_image": has_image
            }
            print(f"Encontrado ID (description): {page_id}, URL: {url}, Título: {title}, Tiene imagen: {has_image}")

            # Si tiene imagen, explorar el enlace "show" y extraer dbCode y txt_totalImagenes
            if has_image:
                show_link = re.search(r'href=["\'](.*?show/.*?)["\']', html_content)
                if show_link:
                    show_url = urljoin(url, show_link.group(1))
                    show_content = curl_request(show_url)
                    print(f"Explorando show URL: {show_url}")  # Log para depuración
                    print(f"Contenido de show: {show_content[:500]}")  # Log para depuración
                    img_match = re.search(r'ViewImage\.do\?.*txt_totalImagenes=(\d*).*dbCode=(\d*)', show_content)
                    if img_match:
                        print(f"{img_match}")
                        db_code = img_match.group(2)
                        total_images = img_match.group(1)
                        urls_description[page_id].update({
                            "db_code": db_code,
                            "total_images": total_images
                        })
                        print(f"Extraído dbCode: {db_code}, txt_totalImagenes: {total_images} para ID: {page_id}")

            # Guardar los resultados en archivos JSON después de actualizar
            with open(description_file, "w") as desc_file:
                json.dump(urls_description, desc_file, indent=4)

    elif "contiene/" in url:
        match = re.search(r'contiene/(\d+)', url)
        if match:
            page_id = match.group(1)
            urls_contiene[page_id] = url
            print(f"Encontrado ID (contiene): {page_id}, URL: {url}")

    # Guardar la URL como procesada y eliminarla de no procesadas si corresponde
    save_processed_page(url)
    processed_pages.add(url)
    currently_processing.remove(url)
    remove_unprocessed_page(url)

    # Guardar los resultados en archivos JSON
    with open(contiene_file, "w") as cont_file:
        json.dump(urls_contiene, cont_file, indent=4)

    # Extraer y explorar solo los enlaces "contiene" y "description"
    links = extract_links(html_content, url)
    if not links:
        print(f"No se encontraron enlaces en: {url}")
        # Si no hay enlaces, buscar otro enlace disponible para continuar
        next_link = get_next_unprocessed_link()
        if next_link:
            explore_links(next_link)
        return
    else:
        print(f"Enlaces encontrados en {url}: {links}")
    for link in links:
        if global_stop:
            print("Exploración detenida. Guardando progreso...")
            return
        if ("description/" in link or "contiene/" in link) and "/imprimir" not in link and "exportEAD/" not in link:
            if link not in processed_pages:
                save_unprocessed_page(link)
                time.sleep(1)  # Añadir un retraso para evitar demasiadas solicitudes en poco tiempo
                explore_links(link)

# Función para extraer enlaces de la página HTML
def extract_links(html, base_url):
    # Ignorar los enlaces dentro de un div con la clase "ramaArbol"
    html = re.sub(r'<div[^>]*class=["\']ramaArbol["\'][^>]*>.*?</div>', '', html, flags=re.DOTALL)
    links = re.findall(r'href=["\'](.*?)["\']', html)
    full_links = [urljoin(base_url, link) for link in links if ("contiene" in link or "description" in link) and "/imprimir" not in link and "exportEAD/" not in link]
    return full_links

# Función para obtener el siguiente enlace no procesado
def get_next_unprocessed_link():
    # Buscar en el archivo de no procesadas
    for page_url in load_unprocessed_pages():
        if page_url not in processed_pages:
            return page_url
    return None

# Determinar la URL inicial para comenzar la exploración
def get_start_url():
    unprocessed_pages = load_unprocessed_pages()
    if unprocessed_pages:
        # Obtener la primera URL no procesada disponible
        return list(unprocessed_pages)[0]
    if processed_pages:
        # Obtener la última URL procesada y determinar si es un enlace contiene o description
        last_processed = list(processed_pages)[-1]
        if "description/" in last_processed or "contiene/" in last_processed:
            print(f"Reiniciando desde la última página procesada: {last_processed}")
            return last_processed
    # Si no hay nada procesado, comenzar desde la ur de abajo
    return "https://pares.mcu.es/ParesBusquedas20/catalogo/description/1235"

start_url = get_start_url()
explore_links(start_url)
