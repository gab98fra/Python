# ----------------------------------------------------------------------------
# Nombre:       get_html.py
# Autor:        Gabriel F
# GitHub:       https://github.com/gab98fra/
# Creado:       30 de Septiembre 2020
# Modificado:   30 de Septiembre 2020
# Copyright:    (c) 2020 by Gabriel F, 2020
# ----------------------------------------------------------------------------

"""
    Obtiene el html de un sitio web a través de su dominio

    Python 3.8.2

"""

#Librería nativa
from http.client import HTTPConnection

import socket
import ssl


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

