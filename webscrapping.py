import re
import csv

# Definir tamaño del buffer y centinela
BUFFER_SIZE = 4096
CENTINELA = '</h5>'  # Usamos el cierre del título de los juegos como referencia

# Expresiones regulares para extraer nombres de juegos y URLs de imágenes
regex_juego = re.compile(r'<h5 class="txt-style-subtitle-bold txt-block-utility__title">(.*?)</h5>')
image_pattern = re.compile(r'<source srcset="(.*?)"')

# Archivo HTML a procesar
archivo_html = 'pagina_ps5.html'
# Buffer para leer el archivo HTML
buffer_size = 1024  # Tamaño del buffer en bytes
buffer = ""
centinela = ""  # Centinela para marcar el final del archivo

# Lista para almacenar los datos extraídos
games_data = []

# Abrir el archivo HTML
with open(archivo_html, "r", encoding="utf-8") as file:
    while True:
        # Leer el archivo en bloques (buffer)
        chunk = file.read(buffer_size)
        if not chunk:
            break  # Centinela: final del archivo
        buffer += chunk

        # Buscar coincidencias en el buffer
        names = regex_juego.findall(buffer)
        images = image_pattern.findall(buffer)

        # Almacenar los datos encontrados
        for name, image in zip(names, images):
            games_data.append((name, image))

        # Limpiar el buffer para evitar duplicados
        buffer = ""

# Guardar los datos en un archivo CSV
csv_file = "juegos.csv"
with open(csv_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Nombre del Juego", "URL de la Imagen"])  # Escribir cabecera
    writer.writerows(games_data)  # Escribir datos

print(f"Datos guardados en {csv_file}")