import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
import os
import json
import time
import subprocess
import random

class ParesFileScraper:
    def __init__(self, base_url="https://pares.mcu.es"):
        self.base_url = base_url
        self.session = requests.Session()
        self.todo_file = "todo_urls.txt"
        self.done_file = "done_urls.txt"
        self.description_file = "description_data.json"
        self.cookie_file = "cookies.txt"
        self.log_file = "log_file.txt"
        self.img_folder = "img"
        self.urls_description = self.load_existing_descriptions()
        self.ensure_files_exist()

    def ensure_files_exist(self):
        for file in [self.todo_file, self.done_file, self.cookie_file, self.log_file]:
            if not os.path.exists(file):
                open(file, 'a').close()
        if not os.path.exists(self.img_folder):
            os.makedirs(self.img_folder)

    def load_existing_descriptions(self):
        if os.path.exists(self.description_file):
            with open(self.description_file, "r", encoding='utf-8') as desc_file:
                return json.load(desc_file)
        return {}

    def save_descriptions(self):
        with open(self.description_file, "w", encoding='utf-8') as desc_file:
            json.dump(self.urls_description, desc_file, indent=4, ensure_ascii=False)

    def add_to_todo(self, urls):
        done_urls = self.get_done_urls()
        with open(self.todo_file, 'a') as f:
            for url in urls:
                if url not in done_urls:
                    f.write(f"{url}\n")

    def get_done_urls(self):
        with open(self.done_file, 'r') as f:
            return set(line.strip() for line in f)

    def mark_as_done(self, url):
        with open(self.done_file, 'a') as f:
            f.write(f"{url}\n")

    def get_next_url(self):
        with open(self.todo_file, 'r') as f:
            lines = f.readlines()

        if not lines:
            return None

        next_url = lines[0].strip()
        
        with open(self.todo_file, 'w') as f:
            f.writelines(lines[1:])

        return next_url

    def get_page(self, url):
        try:
            response = self.session.get(url)
            response.raise_for_status()
            time.sleep(1)
            return response.text
        except requests.RequestException as e:
            self.log_error(f"Error fetching {url}: {e}")
            return None

    def process_description(self, url):
        html_content = self.get_page(url)
        if not html_content:
            return

        match = re.search(r'description/(\d+)', url)
        if match:
            page_id = match.group(1)
            soup = BeautifulSoup(html_content, 'html.parser')

            title_match = soup.find('h4', string=re.compile(r'Titulo Nombre Atribuido:'))
            title = title_match.find_next('p').text.strip() if title_match else ""

            contiene_links = soup.find_all('a', href=re.compile(r'/contiene/\d+'))
            contiene_urls = [urljoin(self.base_url, link['href']) for link in contiene_links]
            if contiene_urls:
                print(f"Found contiene links: {contiene_urls}")
                self.add_to_todo(contiene_urls)

            has_image = False
            img_download_links = []  # Arreglo para almacenar los enlaces de descarga de imágenes
            show_link = soup.find('a', href=re.compile(r'/show/\d+'))
            if show_link:
                has_image = True
                show_url = urljoin(self.base_url, show_link['href'])
                # Obtener cookies desde la página 'show'
                self.get_cookies_from_show(show_url)
                show_content = self.get_page(show_url)
                if show_content:
                    dbcodes = re.findall(r'VisorController.do?.*txt_id_imagen=(\d*)&txt_rotar=0&txt_contraste=0&appOrigen=&dbCode=(\d*)', show_content)
                    img_download_links = [
                        f"https://pares.mcu.es/ParesBusquedas20/ViewImage.do?accion=42&txt_zoom=10&txt_contraste=0&txt_polarizado=&txt_brillo=10.0&txt_contrast=1.0&txt_transformacion=-1&txt_descarga=1&dbCode={dbcode[1]}&txt_id_imagen={dbcode[0]}"
                        for dbcode in dbcodes
                    ]
                    print(f"Generated image download links: {img_download_links}")

                    # Descargar cada imagen y guardarla en la carpeta correspondiente
                    self.download_images(page_id, img_download_links)

            # Almacenar todos los datos en self.urls_description
            self.urls_description[page_id] = {
                "title": title,
                "url": url,
                "has_image": has_image,
                "image_links": img_download_links  # Añadir los enlaces de descarga de imágenes
            }

            self.save_descriptions()
    def log_error(self, message):
        with open(self.log_file, "a", encoding='utf-8') as log:
            log.write(f"{message}\n")

    def get_random_user_agent(self):
    # Lista de User-Agents de diferentes navegadores y dispositivos
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:112.0) Gecko/20100101 Firefox/112.0",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 15_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (Android 11; Mobile; rv:112.0) Gecko/112.0 Firefox/112.0",
        ]
        return random.choice(user_agents)

    def curl_request(self, url, is_contiene=False):
        try:
            if is_contiene:
                # Realizar una solicitud curl para obtener las cookies primero
                get_cookie_command = [
                    "curl",
                    "-sL",
                    "-c", self.cookie_file,
                    "-H", f"User-Agent: {self.get_random_user_agent()}",
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
                    "-H", f"Cookie: {self.get_cookies()}",
                    "-H", "Origin: https://pares.mcu.es",
                    "-H", f"Referer: {url}",
                    "-H", "Sec-Fetch-Dest: empty",
                    "-H", "Sec-Fetch-Mode: cors",
                    "-H", "Sec-Fetch-Site: same-origin",
                    "-H", f"User-Agent: {self.get_random_user_agent()}",
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
                    "-H", f"User-Agent: {self.get_random_user_agent()}",
                    url
                ]
            result = subprocess.run(command, capture_output=True, text=True)
            # Guardar en el archivo de log
            self.log_error(f"URL: {url}\nReturn Code: {result.returncode}\nOutput Length: {len(result.stdout)}\nOutput Preview: {result.stdout[:500]}\n")
            return result.stdout
        except Exception as e:
            self.log_error(f"Error fetching {url}: {e}")
            return ""
    def get_cookies(self):
        cookies = []
        if os.path.exists(self.cookie_file):
            with open(self.cookie_file, "r") as f:
                for line in f:
                    if not line.startswith("#") and line.strip():
                        parts = line.strip().split("\t")
                        if len(parts) >= 7:
                            cookies.append(f"{parts[5]}={parts[6]}")
                            print(cookies)
        return "; ".join(cookies)

    def get_cookies_from_show(self, show_url):
        command = [
            "curl",
            "-s",
            "-c", self.cookie_file,
            "-H", f"User-Agent: {self.get_random_user_agent()}",
            show_url
        ]
        subprocess.run(command)

    def download_images(self, page_id, img_links):
        # Crear una carpeta específica para las imágenes de esta descripción
        img_dir = os.path.join(self.img_folder, page_id)
        if not os.path.exists(img_dir):
            os.makedirs(img_dir)

        # Descargar cada imagen utilizando cURL con las cookies
        for idx, img_url in enumerate(img_links):
            img_path = os.path.join(img_dir, f"image_{idx + 1}.jpg")
            command = [
                "curl",
                "-s",
                "-b", self.cookie_file,
                "-o", img_path,
                "-H", f"User-Agent: {self.get_random_user_agent()}",
                img_url
            ]
            subprocess.run(command)
            print(f"Downloaded image: {img_path}")

    def log_error(self, message):
        with open(self.log_file, "a", encoding='utf-8') as log:
            log.write(f"{message}\n")

    def process_contiene(self, url):
        html = self.curl_request(url, is_contiene=True)
        time.sleep(2)
        if not html:
            return
        
        soup = BeautifulSoup(html, 'html.parser')
        desc_links = soup.find_all('a', href=re.compile(r'/description/\d+'))
        desc_urls = [urljoin(self.base_url, link['href']) for link in desc_links]

        if desc_urls:
            print(f"Found description links: {desc_urls}")
            self.add_to_todo(desc_urls)

    def process_archive(self):
        while True:
            url = self.get_next_url()
            if not url:
                break

            done_urls = self.get_done_urls()
            if url in done_urls:
                print(f"Skipping processed URL: {url}")
                continue

            print(f"Processing: {url}")
            if "description/" in url:
                self.process_description(url)
            elif "contiene/" in url:
                self.process_contiene(url)
            self.mark_as_done(url)

if __name__ == "__main__":
    scraper = ParesFileScraper()
    scraper.process_archive()
