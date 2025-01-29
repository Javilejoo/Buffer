import re
import csv

# Definir tamaño del buffer
BUFFER_SIZE = 4096  

# Expresiones regulares para extraer nombres de juegos y URLs de imágenes
regex_juego = re.compile(r'<h5 class="txt-style-subtitle-bold txt-block-utility__title">(.*?)</h5>')
regex_imagen = re.compile(r'<source srcset="(.*?)"')

# Archivo HTML a procesar
archivo_html = 'pagina_ps5.html'
csv_file = "juegos.csv"

# Abrir archivo CSV y escribir la cabecera
with open(csv_file, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Nombre del Juego", "URL de la Imagen"])  # Cabecera del archivo CSV

    # Abrir el archivo HTML y procesar en bloques
    with open(archivo_html, "r", encoding="utf-8") as file:
        buffer = ""  # Inicializar buffer
        juegos_guardados = set()  # Evita duplicados de nombres

        while True:
            chunk = file.read(BUFFER_SIZE)
            if not chunk:
                break  # Final del archivo
            buffer += chunk

            # Buscar coincidencias en el buffer
            names = regex_juego.findall(buffer)
            images = regex_imagen.findall(buffer)

            # Guardar los datos encontrados
            for name, image in zip(names, images):
                if name not in juegos_guardados:  # Evita duplicados
                    writer.writerow([name, image])  # Escribir en el CSV
                    juegos_guardados.add(name)  # Registrar en el set
                    print(f"Guardado: {name} - {image}")  # Depuración

            # Mantener solo el final del buffer para evitar cortes en coincidencias
            buffer = buffer[-len(chunk):]  

print(f"Se guardaron {len(juegos_guardados)} juegos en {csv_file}")
