# ----------------------------------------------------------------------------
# Nombre:       crud_sqlserver.py
# Autor:        Gabriel F
# Creado:       12 de Septiembre 2020
# Modificado:   12 de Septiembre 2020
# Copyright:    (c) 2020 by Gabriel F, 2020
# ----------------------------------------------------------------------------

"""
Permite conexión a SQL Server y realizar CRUD

"""

import pyodbc


class sqlserver(self):

    def login(self):
        # localhost, puede va la direccion ip del servicio. eg. 127.0.0.1
        direccion_servidor = 'localhost'
        nombre_bd = 'farmacia'
        nombre_usuario = 'usuario1'
        password = '12345'

        try:  # si la conexión es exitosa
            conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                              direccion_servidor + ';DATABASE=' + nombre_bd + ';UID=' + nombre_usuario + ';PWD='+password)
        except Exception as e:
        #Error
            print("Ocurrió un Error al conectarse a SQL Server: ", e)
    def create(self):
        pass

    def read(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass


if __name__ == "__main__":
    pass
