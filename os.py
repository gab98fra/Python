# ----------------------------------------------------------------------------
# Nombre:       os.py
# Autor:        Gabriel F
# GitHub:       https://github.com/gab98fra/
# Creado:       27 de Octubre 2020
# Modificado:   27 de Octubre 2020
# Copyright:    (c) 2020 by Gabriel F, 2020
# ----------------------------------------------------------------------------


import os
import subprocess

"""

    El siguiente script permite interactuar con el sistema operativo, 
    utilizando algunas particularidades del módulo OS y subprocess

    Python 3.8.2

"""


#retorna la ruta actual
path=os.getcwd()
print("Se encuentra en la siguiente ruta: "+path)


#Muestra en una lista los archivos disponibles del directorio actual
print("\n")
print(os.listdir())

#Cambia a la ruta indicada
os.chdir("C:/Users/user1\Desktop/Python")

#crea una carpeta llamada carpeta nueva
os.system("mkdir carpeta_nueva")

#Cambia el nombre de la carpeta_nueva
os.renames("Carpeta_nueva", "Carpeta_actualizado")

#Otra forma de crear una carpeta
os.mkdir("nueva_carpeta")

#Eliminar carpeta creada
os.rmdir("nueva_carpeta")

#Devuelve el número de cpu del sistema
print(os.cpu_count())

#Devuelve el nombre de usuario de la cuenta de windows
print(os.getlogin())

#revisar características de un archivo en particular
print(os.stat("os.py"))

#ejecutar un comando del sistema
os.system("ping www.google.com")


#Captura la salida del comando dir
info=subprocess.Popen("dir", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
print(info.stdout.read())#salida
print(info.stderr.read())#error

