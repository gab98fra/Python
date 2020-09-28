# ----------------------------------------------------------------------------
# Nombre:       excel.py
# Autor:        Gabriel F
# GitHub:       https://github.com/gab98fra/
# Creado:       27 de Septiembre 2020
# Modificado:   27 de Septiembre 2020
# Copyright:    (c) 2020 by Gabriel F, 2020
# ----------------------------------------------------------------------------

"""
    Permite escribir y exportar datos en archivo excel

    Python 3.8.2
    Pandas 1.1.2

"""

import pandas as pd


def export_excel(path):
    
    #Datos
    data=pd.DataFrame({
                    "Frutas_1":['manzana', 'pera', 'sandia'], #Columna 1
                    "Frutas_2":['manzana', 'pera', 'sandia'], #Columna 2
                    "Frutas_3":['manzana', 'pera', 'sandia'], #Columna 3
                    "Frutas_4":['manzana', 'pera', 'sandia'], #Columna 4
                    "Frutas_5":['manzana', 'pera', 'sandia'], #Columna 5
                    "Frutas_6":['manzana', 'pera', 'sandia'], #Columna 6
                    "Frutas_7":['manzana', 'pera', 'sandia'], #Columna 7
                    "Frutas_8":['manzana', 'pera', 'sandia'], #Columna 8
                    "Frutas_9":['manzana', 'pera', 'sandia'], #Columna 9
                    "Frutas_10":['manzana', 'pera', 'sandia'], #Columna 10
                        })

    
    #Indicamos la dirección
    writer=pd.ExcelWriter(path)#engine='xlsxwriter'  ---opcional
    
    #Exportamos
    data.to_excel(writer, sheet_name="sheet1")
    
    #Guardamos
    writer.save()

if __name__ == "__main__":
    
    export_excel("data.xlsx")