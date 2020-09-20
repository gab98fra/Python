# ----------------------------------------------------------------------------
# Nombre:       crud_sqlserver.py
# Autor:        Gabriel F
# GitHub:       https://github.com/gab98fra/
# Creado:       15 de Septiembre 2020
# Modificado:   20 de Septiembre 2020
# Copyright:    (c) 2020 by Gabriel F, 2020
# ----------------------------------------------------------------------------

"""
Permite conexión a SQL Server y realizar CRUD

"""

import pyodbc


class sqlserver(object):

    def login(self):
        
        #Variables - datos del servidor
        server1 = 'localhost'
        name_bd = 'farmacia'
        name_user = 'useradm'
        password = '938477ndm'

        try:
            # Conexión al servidor
            conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                              server1 + ';DATABASE=' + name_bd + ';UID=' + name_user + ';PWD='+password)
            return conexion

        except Exception as e:
        # Error
            print("Ocurrió un error al conectarse a SQL Server: ", e)

    def create(self, conexion):

        if conexion:
            try:
                with conexion.cursor() as cursor:

                    query = "INSERT INTO venta(venta, piezas_Vendidas, id_medicamento) VALUES (  ?,?,?)"
                    
                    # Ingresar los datos en la tabla venta
                    cursor.execute(query, (234, 2345, 2))
                    cursor.execute(query, (232, 45, 2))
                    cursor.execute(query, (232, 25, 2))
                    cursor.execute(query, (432.2, 34, 2))

            except Exception as e:

                print("Ocurrió un error", e)

            finally:
                conexion.close()

        else:
            print("No hay conexión a SQL Server")

    def read(self, conexion):
        if conexion:
            try:
                with conexion.cursor() as cursor:  
                
                    # sintax de SQL
                    cursor.execute("SELECT id_venta, venta, piezas_Vendidas, id_medicamento from venta")

                    ventas_consulta = cursor.fetchall()

                
                    for filas in ventas_consulta:
                    #imprimir valores encontrados
                        print(filas)

            except Exception as e:
                print("Ocurrió un error", e)

            finally:  
                conexion.close()  

        else:
            print("No hay conexión a SQL Server")

    def update(self, conexion):
        if conexion:
            try:
              with conexion.cursor() as cursor:
                
                query="UPDATE venta set id_medicamento=? where id_venta=?"
                
                #Variables
                nuevo_id_medicamento=4 
                id_venta=13

                cursor.execute(query,(nuevo_id_medicamento, id_venta))

                conexion.commit()

            except Exception as e:
                print ("Ocurrió un error",e)

            finally:

                conexion.close()

        else:
            print ("No hay conexión a SQL Server")


    def delete(self, conexion):
        if conexion:
            try:
                with conexion.cursor() as cursor:
                
                    query="DELETE from venta  where id_venta > ?"
                    #variable
                    nuevo_id_venta=13
                
                    cursor.execute(query,(nuevo_id_venta))
                    
                    conexion.commit()

            except Exception as e:
                print ("Ocurrió un error",e)

            finally:

                conexion.close()

        else:
            print ("No hay conexión a SQL Server")
            

if __name__ == "__main__":
    objetct1=sqlserver()
    conexion=objetct1.login()
    print ("Conexión correcta")

    """"
    object1.create(conexion)
    object1.read(conexion)
    object1.update(conexion)
    object1.delete(conexion)

    """"
