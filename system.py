# ----------------------------------------------------------------------------
# Nombre:       system.py
# Autor:        Gabriel F
# GitHub:       https://github.com/gab98fra/
# Creado:       30 de Septiembre 2020
# Modificado:   30 de Septiembre 2020
# Copyright:    (c) 2020 by Gabriel F, 2020
# ----------------------------------------------------------------------------

"""
    El siguiente scrip realiza lo siguiente:

        Detecta las características del OS y la ip de la máquina que estemos utilizando:
        sistema operativo, versión, arquitectura, nombre del dispositivo, etc.
    
        Obtner de ip de una página web, ejemplo: google

    Python 3.8.2

"""

#Librerías nativas
import platform
import socket

class info_os(object):
#Información del sistema operativo

    def __init__(self):
        
        #Información a buscar
        self.info=['system','uname', 'version','release', 
                
                'architecture', 'linux_distribution',
                
                'mac_ver', 'machine', 'node', 'platform','processor',
                
                'python_build', 'python_compiler','python_version',
                    ]

        self.get_data_os()

    def get_data_os(self):
    #Obtención de la información

        for info in self.info:

            if hasattr(platform, info):
                
                data=(info, getattr(platform, info)())
                
                print(data)


class info_ip(object):
#Información ip

    def __init__(self):

        self.get_ip()
    
    def get_ip(self):
        
        #Nombre del dispositivo
        name_device=socket.gethostname()
        
        #Obtener ip de la máquina
        print(socket.getprotobyname(name_device))
        
        #Obtener la ip de una página web
        print(socket.getaddrinfo("google.com", 80) )

if __name__ == "__main__":
   
    print("=================Datos encontrados del OS=====================")
    
    object1=info_os()
    
    print("=================Fin==========================================\n")

    print("=================Datos de ip  ================================")
    
    object2=info_ip()
    
    print("=================Fin==========================================\n")
            

