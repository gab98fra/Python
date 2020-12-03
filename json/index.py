# ----------------------------------------------------------------------------
# Nombre:       index.py
# Autor:        Gabriel F
# GitHub:       https://github.com/gab98fra/
# Creado:       02 de diciembre  2020
# Modificado:   03 de diciembre  2020
# Copyright:    (c) 2020 by Gabriel F, 2020
# ----------------------------------------------------------------------------


"""
    El script permite trabajar con archivos json utilizando POO:
        -Leer datos desde un archivo JSON
        -Guardar o exportar datos a un archivo JSON

    Python 3.8.2

"""

#Librería nativa
import json

class file_json():

    def __init__(self):

        #Ruta del archivo json
        self.path="file.json"
    
    def read(self):
    #Lectura de archivo json / exportar datos en un archivo json
       
        with open(self.path) as read_file:
            
            #diccionarios en forma de lista
            data_json=json.load(read_file)
            print(data_json,"\n")

            #Acceder por elemento
            for info in data_json:
                
                f_name=info.get("Nombre", "")#"" si no lo encuentra regresa vacío
                l_name=info.get("Apellido", "")
                job=info.get("Puesto")

                print("Nombre: ", f_name)
                print(f"Apellido: {l_name}")
                print(f"Puesto: {job}"+ "\n")
            
            #Exportar datos a un archivo JSON, enviado los datos 
            self.save(data_json)

    def save(self, data):
    #Guarda o exporta los datos a un archivo json

        with open("save_file.json", "w") as write_file:
            json.dump(data, write_file)



if __name__ == "__main__":
    
    #Objecto
    object_json=file_json()
    object_json.read()


