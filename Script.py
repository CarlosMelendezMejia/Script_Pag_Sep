import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Constantes
TAG_BOOKS = ('LMP', 'MLA', 'PAA', 'PCA', 'PEA', 'SDA', 'TPA', 'CMA', 'SHA')
BASE_URL = 'https://www.conaliteg.sep.gob.mx/2023/c/'
BASE2_URL = 'https://www.conaliteg.sep.gob.mx/2023/'
MAX_IMAGES_PER_BOOK = 400

def download_images(book_url, output_folder):
    # Crea la carpeta de salida si no existe
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    base = "000"
    # Itera a través del rango de imágenes por libro
    for img_cont in range(1, MAX_IMAGES_PER_BOOK + 1):
        img_num = f"{base}{img_cont}"[-len(base):]
        img_url = f'{book_url}{img_num}.jpg'
        img_name = img_url.split('/')[-1]
        img_path = os.path.join(output_folder, img_name)

        # Realiza la solicitud HTTP para descargar la imagen
        response = requests.get(img_url)
        if response.status_code == 200:
            # Guarda la imagen en el archivo local
            with open(img_path, 'wb') as img_file:
                img_file.write(response.content)
            print(f'Imagen descargada: {img_name}')
        else:
            # Si no se puede descargar la imagen, sale del bucle
            break

def main():
    # Itera a través de los índices de P y los tipos de libros
    for i in range(8):
        for tag in TAG_BOOKS:
            try:
                # Construye las URL para buscar libros y descargar imágenes
                book_url = f'{BASE_URL}P{i}{tag}/'
                book_search_url = f'{BASE2_URL}P{i}{tag}.htm#page/2'

                # Realiza la solicitud HTTP para buscar libros
                response = requests.get(book_search_url)
                response.raise_for_status()

                # Analiza el contenido HTML de la página
                soup = BeautifulSoup(response.content, 'html.parser')
                img_tags = soup.find_all('img')

                # Define la carpeta de salida y la ruta absoluta
                output_folder = f'P{i}{tag}'
                absolute_path = os.path.abspath(output_folder)

                # Descarga las imágenes del libro
                download_images(book_url, output_folder)

                # Imprime mensajes al completar la descarga
                print('Descarga completada.')
                print(f'Ruta absoluta de la carpeta de imágenes descargadas: {absolute_path}')

            except requests.exceptions.RequestException as e:
                # Maneja la excepción si no se encuentra el libro
                print(f'No existe el libro {book_url}: {e}')
                continue

if __name__ == "__main__":
    main()
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Constantes
TAG_BOOKS = ('LMP', 'MLA', 'PAA', 'PCA', 'PEA', 'SDA', 'TPA', 'CMA', 'SHA')
BASE_URL = 'https://www.conaliteg.sep.gob.mx/2023/c/'
BASE2_URL = 'https://www.conaliteg.sep.gob.mx/2023/'
MAX_IMAGES_PER_BOOK = 400

def download_images(book_url, output_folder):
    # Crea la carpeta de salida si no existe
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    base = "000"
    # Itera a través del rango de imágenes por libro
    for img_cont in range(1, MAX_IMAGES_PER_BOOK + 1):
        img_num = f"{base}{img_cont}"[-len(base):]
        img_url = f'{book_url}{img_num}.jpg'
        img_name = img_url.split('/')[-1]
        img_path = os.path.join(output_folder, img_name)

        # Realiza la solicitud HTTP para descargar la imagen
        response = requests.get(img_url)
        if response.status_code == 200:
            # Guarda la imagen en el archivo local
            with open(img_path, 'wb') as img_file:
                img_file.write(response.content)
            print(f'Imagen descargada: {img_name}')
        else:
            # Si no se puede descargar la imagen, sale del bucle
            break

def main():
    # Itera a través de los índices de P y los tipos de libros
    for i in range(8):
        for tag in TAG_BOOKS:
            try:
                # Construye las URL para buscar libros y descargar imágenes
                book_url = f'{BASE_URL}P{i}{tag}/'
                book_search_url = f'{BASE2_URL}P{i}{tag}.htm#page/2'

                # Realiza la solicitud HTTP para buscar libros
                response = requests.get(book_search_url)
                response.raise_for_status()

                # Analiza el contenido HTML de la página
                soup = BeautifulSoup(response.content, 'html.parser')
                img_tags = soup.find_all('img')

                # Define la carpeta de salida y la ruta absoluta
                output_folder = f'P{i}{tag}'
                absolute_path = os.path.abspath(output_folder)

                # Descarga las imágenes del libro
                download_images(book_url, output_folder)

                # Imprime mensajes al completar la descarga
                print('Descarga completada.')
                print(f'Ruta absoluta de la carpeta de imágenes descargadas: {absolute_path}')

            except requests.exceptions.RequestException as e:
                # Maneja la excepción si no se encuentra el libro
                print(f'No existe el libro {book_url}: {e}')
                continue

if __name__ == "__main__":
    main()
