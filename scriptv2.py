import requests
from bs4 import BeautifulSoup

def obtener_urls_dva(url_base, rango_inicio, rango_fin):
    urls_encontradas = []

    for i in range(rango_inicio, rango_fin + 1):
        url = f"{url_base}{i}/" if i > 0 else url_base

        # SOLICITUD HTTP
        response = requests.get(url)
        # analizarHTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # buscar discussion-row
        discussion_rows = soup.find_all('div', class_='discussion-row')
        
        # Iterar a través de cada 'discussion-row'
        for row in discussion_rows:
            link = row.find('a', class_='discussion-link')
            if link and 'Developer Associate topic' in link.text:
                url_completa = f"https://www.examtopics.com{link['href']}"
                urls_encontradas.append(url_completa)

        
        print(f"Procesada página {i} de {rango_fin}")

    return urls_encontradas

# URL base
url_base = "https://www.examtopics.com/discussions/amazon/"

# Definir lotes de procesamiento
lote_tamano = 50
numero_paginas = 581

for inicio in range(0, numero_paginas, lote_tamano):
    fin = min(inicio + lote_tamano, numero_paginas)
    urls_dva = obtener_urls_dva(url_base, inicio, fin)

    # Guardar las URLs en un archivo
    with open('developer_topics.txt', 'a') as archivo:
        for url in urls_dva:
            archivo.write(url + '\n')

    print(f"Guardadas URLs de las páginas {inicio} a {fin} en 'urls_dva.txt'")
