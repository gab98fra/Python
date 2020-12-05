# ----------------------------------------------------------------------------
# Nombre:       index.py
# Autor:        Gabriel F
# GitHub:       https://github.com/gab98fra/
# Creado:       04 de diciembre 2020
# Modificado:   05 de diciembre 2020
# Copyright:    (c) 2020 by Gabriel F, 2020
# ----------------------------------------------------------------------------

"""
    Funciones básicas para trabajar con APIS
    Métodos:
        -GET
        -POST
        -HEADERS
        -PUT -  actualizar
        -DELETE
        -Descargar una imagen y video

    python 3.8.2
    requests 2.25.0
    https://httpbin.org/#/HTTP_Methods

"""

import requests
import json


def get_html():
#Método: get - args

    url="https://httpbin.org/get"

    #Parámetro a enviar
    args={
        'name':"John",
        'nickname':'Jo_03',
        'age':2010
    }
    
    #Enviar parámetro
    response=requests.get(url, params=args)

    if response.status_code==200:
        
        #Obtener Estructura html
        html=response.content        

        print(html)

        #Obtener la url
        print("\n", response.url)
    

def post ():
#Método: post -  data

    url="https://httpbin.org/post"

    #Parámetro a enviar
    payload={
        'name':"John",
        'nickname':'Jo_03',
        'age':2010
    }
    
    #Enviar parámetro
    response=requests.post(url, json=payload)#Los datos se incrustan en data

    if response.status_code==200:
        
        #Obtener el contenido
        content=response.content        

        print(content)

        #Obtener la url: se mantien oculto los parámetros enviados
        print("\n", response.url)
    

def header ():
#Encabezaados - headers

    url="https://httpbin.org/post"

    #Parámetro a enviar
    payload={
        'name':"John",
        'nickname':'Jo_03',
        'age':2010
    }
    
    #Indicar el envío en formato json
    headers={
        'Content-Type':"application/json",
        "access-token":"abcd",
    }

    #enviar parámetros
    response=requests.post(url, json=payload, headers=headers)

    if response.status_code==200:
        
        #Leer el contenido del encabezado
        headers_response=response.headers#diccionario
        print(headers_response)

        #obtener el server
        print(headers_response["server"])

def put():
#Método PUT
    
    url="https://httpbin.org/put"

    #Parámetro a enviar
    payload={
        'name':"John",
        'nickname':'Jo_03',
        'age':2010
    }

    #enviar parámetros
    response=requests.put(url, json=payload)

    if response.status_code==200:
        
        #Leer el contenido del
        content=response.content
        
        print(content)

        #obtener la url
        print(response.url)

def delete():
#Método PUT
    
    url="https://httpbin.org/delete"

    #Parámetro a enviar
    payload={
        'name':"John",
        'nickname':'Jo_03',
        'age':2010
    }

    #enviar parámetros
    response=requests.delete(url, json=payload)

    if response.status_code==200:
        
        #Leer el contenido del
        content=response.content
        
        print(content)

        #obtener la url
        print(response.url)



if __name__ == "__main__":
    #get_html()
    #post()
    #header()
    #put()
    #delete()
