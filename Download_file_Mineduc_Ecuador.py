import urllib.request  #El módulo urllib. request es usado principalmente para buscar y abrir URLs.
import os #nos permite manipular los archivos del directorio
def download_file(url):
    file = input("Ingrese el nombre del archivo con su extensión) \n>")
    try:
        r = urllib.request.urlopen(url)
        f = open(file, "wb")
        f.write(r.read())
        f.close()
    except Exception:
        url = input("Error en la url  vuelva a introducir nuevamente\n> ")
        download_file(url)

url = input("Introduzca la url del archivo a descargar \n>")

download_file(url)
