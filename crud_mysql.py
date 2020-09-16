# ----------------------------------------------------------------------------
# Nombre:       crud_mysql.py
# Autor:        Gabriel F
# Creado:       16 de Septiembre 2020
# Modificado:   16 de Septiembre 2020
# Copyright:    (c) 2020 by Gabriel F, 2020
# ----------------------------------------------------------------------------

"""
Permite conexión a mysql y realizar CRUD

"""

import mysql.connector


class mysql_conect(object):

  def __init__(self):

    self.conexion=""
    
    self.login()

  def login(self):

    try:

      self.conexion=mysql.connector.connect(host="localhost", user="root", passwd="", database="farmacia")
      
      datos=self.conexion.cursor()
      
      datos.execute("show tables")

      for base in datos:
        print(base)

      #self.conexion.close()

      return True

    except:
      print("Ocurrió un error al momento de conectarse")
      return False
  
  def create(self):
    
    if self.conexion:

      try:

        cursor=self.conexion.cursor()
        
        query="insert into empleados(empleado, apell_pat, apell_mat, ciudad, id_sexo) values (%s, %s, %s, %s, %s)"
        
        datos=("Carlos", "HSR", "HSR", "ciudad1", 1)
        
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
        
        cursor.execute("select * from empleados")
        
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
        
        query="update empleados set ciudad=%s, id_sexo=%s where id_empleado=%s"
        datos=("nueva ciudad", 2, 5)

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
        
        query="delete from empleados where empleado=%s and id_empleado=%s"
        dato=("Antonio", 3)

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

    #objeto.create()
    #objeto.read()
    #objeto.update()
    #objeto.delete()
