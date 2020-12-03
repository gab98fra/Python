# ----------------------------------------------------------------------------
# Nombre:       index.py
# Autor:        Gabriel F
# GitHub:       https://github.com/gab98fra/
# Creado:       02 de diciembre  2020
# Modificado:   02 de diciembre  2020
# Copyright:    (c) 2020 by Gabriel F, 2020
# ----------------------------------------------------------------------------


"""
    El script permite trabajar con archivos json utilizando POO

    Python 3.8.2

"""

#Librería nativa
import json

class file_json():

    def __init__(self):

        #Ruta del archivo json
        self.path="file.json"
    
    def read(self):
    #Lectura de archivo json
       
        with open(self.path) as data:
            #diccionarios en forma de lista
            info_json=json.load(data)
            print(info_json,"\n")

            #Acceder por elementos
            for info in info_json:
                print("nombre: ",info.get("Nombre", ""))#"" si no lo encuentra regresa vacío
                print("Apellido: ",info.get("Apellido", ""))
                print("Pueto: ",info.get("Puesto"), "\n")
        



if __name__ == "__main__":
    
    #Objecto
    object_json=file_json()
    object_json.read()


