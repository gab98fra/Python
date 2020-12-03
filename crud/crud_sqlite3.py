# ----------------------------------------------------------------------------
# Nombre:       crud_sqlite3.py
# Autor:        Gabriel F
# GitHub:       https://github.com/gab98fra/
# Creado:       15 de Septiembre 2020
# Modificado:   05 de Octubre 2020
# Copyright:    (c) 2020 by Gabriel F, 2020
# ----------------------------------------------------------------------------

"""
Permite conexión a SQLite3 y realizar CRUD

"""


import sqlite3


class sqlite3_bd():

    def login(self):
        
        conexion = sqlite3.connect("bd1.db")

        try:
            conexion.execute("""create table venta (
                              id_venta integer primary key autoincrement,
                              descripcion text,
                              precio real
                        )""")

            print("se creo la tabla venta")

            return conexion
        except sqlite3.OperationalError:

            print("La tabla venta ya existe")
            return conexion

    def create(self, conexion):

        if conexion:

            conexion.execute("insert into venta(descripcion,precio) values (?,?)", ("naranjas", 23.50))
            conexion.execute("insert into venta(descripcion,precio) values (?,?)", ("peras", 34))
            conexion.execute("insert into venta(descripcion,precio) values (?,?)", ("bananas", 25))
            
            print("Se guardaron correctamente los datos")
            
            conexion.commit()
            conexion.close()
        else:
            print ("No se guardaron los datos en la tabla")

    def read(self, conexion):
        
        if conexion:
            cursor=conexion.execute("select id_venta,descripcion,precio from venta")
            for fila in cursor:
                print(fila)
        
            conexion.close()

    
    def update(self, conexion):

        if conexion:
            conexion.execute("UPDATE venta set descripcion=?, precio=? where id_venta=?", ("manzana", 21.50, 1))
            conexion.execute("UPDATE venta set descripcion=?, precio=? where id_venta=?", ("sandia", 5.60, 2))
            conexion.execute("UPDATE venta set descripcion=?, precio=? where id_venta=?", ("melon", 22.30, 2))

            print ("Se actualizaron correctamente los datos")

            conexion.commit()
            conexion.close()

    def delete(self, conexion):

        if conexion:
            conexion.execute("DELETE FROM venta WHERE id_venta=?", ("3"))
            
            print("Se eliminó el dato indicado")

            conexion.commit()
            conexion.close()


if __name__ == "__main__":
    login1=sqlite3_bd()
    
    conexion=login1.login()
    """
    login1.create(conexion)
    login1.read(conexion)
    login1.update(conexion)
    login1.delete(conexion)
    """

    