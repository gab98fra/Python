# ----------------------------------------------------------------------------
# Nombre:       get_html.py
# Autor:        Gabriel F
# GitHub:       https://github.com/gab98fra/
# Creado:       30 de septiembre 2020
# Modificado:   04 de diciembre 2020
# Copyright:    (c) 2020 by Gabriel F, 2020
# ----------------------------------------------------------------------------

"""
    Obtiene el html de un sitio web a través de su dominio

    python 3.8.2
    requests 2.25.0

"""

#Librerías nativas
from http.client import HTTPConnection
import socket
import ssl


def get_html_1():
#fORMA 1:
    hostname='google.com'

    #Creamos el contexto
    context=ssl.create_default_context()

    with socket.create_connection((hostname, 443)) as sock:
        
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:

            conn=HTTPConnection(hostname)
            conn.request('GET', '/')

            r1=conn.getresponse()

            print(r1.read())
            conn.close()


import requests


def get_html_2():
#Otra forma de obtener la estructura de html de un sitio

    url="https://google.com.mx"

    #Obtener respuesta
    response=requests.get(url)
    
    if response.status_code==200:
        
        #Estructura html
        html=response.content        
        
        #guardar en un archivo txt
        file=open("site.html", 'wb')
        file.write(html)
        file.close()

if __name__ == "__main__":
    
    get_html_1()
    get_html_2()