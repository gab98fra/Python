# ----------------------------------------------------------------------------
# Nombre:       crud_postgresql.py
# Autor:        Gabriel F
# GitHub:       https://github.com/gab98fra/
# Creado:       16 de Septiembre 2020
# Modificado:   20 de Septiembre 2020
# Copyright:    (c) 2020 by Gabriel F, 2020
# ----------------------------------------------------------------------------

"""
Permite conexión a PostgreSQL y realizar CRUD

"""
import psycopg2


class postgresql(object)
    
    def __init__(self):

        self.conexion=""
        
        self.login()

    def login(self):

        try:

            self.conexion=psycopg2.connect(database="tienda", user="postgres", password="heladera")
            
            print("Conexion correcta")
            return True

        except:
            print("Ocurrió un error al momento de conectarse")
            return False
    
    def create(self):
        
        if self.conexion:

            try:

                cursor=self.conexion.cursor()
                
                query="insert into articulos(articulo, precio) values (%s,%s)"
                
                datos=("naranjas", 23.50)
                
                cursor.execute(query, datos)
                
                print ("Dato ingresado en la BD")
                
                self.conexion.commit()
                self.conexion.close() 

                return True

            except:
                print("Ocurrio un error al momento de conectarse")
                return False
        
    def read(self):

        if self.conexion:

            try:

                cursor=self.conexion.cursor()
                
                cursor.execute("select * from articulos")
                
                for datos in cursor:
                print (datos)
                
                self.conexion.close() 

                return True

            except:
                print("Ocurrió un error al momento de conectarse")
                return False

    def update(self):

        if self.conexion:

            try:

                cursor=self.conexion.cursor()
                
                query="update articulos set articulo=%s  where id_articulo=%s"
                datos=("dulces", 5)

                cursor.execute(query, datos)
                print("Se actualizó el dato")
                
                self.conexion.commit()
                self.conexion.close() 

                return True

            except:
                print("Ocurrió un error al momento de conectarse")
                return False
    
    def delete(self):
        
        if self.conexion:

            try:

                cursor=self.conexion.cursor()
                
                query="delete from articulos where articulo=%s and id_articulo=%s"
                dato=("paletas", 3)

                cursor.execute(query, dato)

                print("se elimió correctamente el dato")        

                self.conexion.commit()        
                self.conexion.close() 

                return True

            except:
                print("Ocurrió un error al momento de conectarse")
                return False
  

if __name__ == "__main__":
    
    objeto=mysql_conect()
    """
    objeto.create()
    objeto.read()
    objeto.update()
    objeto.delete()
    """
    