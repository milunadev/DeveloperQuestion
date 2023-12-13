import webbrowser

def abrir_urls_por_grupo(archivo, grupo):
    cantidad_por_grupo = 10
    inicio = (grupo - 1) * cantidad_por_grupo
    fin = inicio + cantidad_por_grupo

    with open(archivo, 'r') as file:
        urls = file.readlines()[inicio:fin]

    for url in urls:
        webbrowser.open_new_tab(url.strip())

archivo_urls = 'urls_dva.txt'  # Nombre de tu archivo
grupo_deseado = 34
  # Cambia esto al grupo que deseas abrir (1, 2, 3, etc.)
#27
abrir_urls_por_grupo(archivo_urls, grupo_deseado)

#REVISAR 7