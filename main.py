import requests
from bs4 import BeautifulSoup

def obtener_urls_dva(url_base, numero_paginas):
    urls_encontradas = []

    for i in range(numero_paginas + 1):
        # Construir la URL
        if i == 0:
            url = url_base
        else:
            url = f"{url_base}{i}/"

        # Realizar la solicitud HTTP
        response = requests.get(url)
        # Analizar el HTML de la respuesta
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Buscar todos los 'discussion-row' dentro del contenedor 'discussion-list'
        discussion_rows = soup.find_all('div', class_='discussion-row')
        
        # Iterar a través de cada 'discussion-row'
        for row in discussion_rows:
            # Buscar el enlace dentro de 'discussion-row'
            link = row.find('a', class_='discussion-link')
            if link and 'DVA' in link.text:
                # Construir la URL completa
                url_completa = f"https://www.examtopics.com{link['href']}"
                urls_encontradas.append(url_completa)
    
    return urls_encontradas

# URL base
url_base = "https://www.examtopics.com/discussions/amazon/"

# Número máximo de páginas a recorrer
numero_paginas = 581

# Obtener las URLs
urls_dva = obtener_urls_dva(url_base, numero_paginas)

# Guardar las URLs en un archivo
with open('urls_dva.txt', 'a') as archivo:
    for url in urls_dva:
        archivo.write(url + '\n')

print("Las URLs se han guardado en el archivo 'urls_dva.txt'")
