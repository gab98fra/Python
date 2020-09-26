# ----------------------------------------------------------------------------
# Nombre:       send_email.py
# Autor:        Gabriel F
# GitHub:       https://github.com/gab98fra/
# Creado:       22 de Septiembre 2020
# Modificado:   25 de Septiembre 2020
# Copyright:    (c) 2020 by Gabriel F, 2020
# ----------------------------------------------------------------------------

"""
    Envía correos electrónicos de manera automática, desde una cuenta de gmail.
    Importante configurar su cuenta de gmail (aplicaciones no seguras) antes de ejecutar el script

    Python 3.8.2

"""

#Librerías nativas de python
import smtplib, ssl
from getpass import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.encoders import encode_base64

class send_email(object):

    def __init__(self):
        #---------------Ingresar datos en consola-------------------
        self.email=input("Escriba su email: ")
        self.password=getpass("Escriba su password: ")#getpass, oculta los datos ingresados en pantalla

        #Ingresa los datos receptor
        self.email_2=input("Escriba el email destinatario: ")
        self.subject=input("Escriba el asunto del mensaje: ")
        
        self.message_email()

    def message_email(self):

        #Formato de mensaje
        message=MIMEMultipart('alternative')
        message['Subject']=self.subject
        message['From']=self.email
        message['To']=self.email_2

        message_html=f""" 
        <html>
        <body>
            <h1>Hola {self.email_2} </h1>
            <p>Este es un mensaje enviado desde un sript de Python. ¡¡¡No temas!!!!</p>
            </br></br>En el adjunto encontrá un pequeño imagen
        </body>
        </html>
        """

        #Cuerpo del mensaje
        body=MIMEText(message_html, "html")

        #Agregar contenido al mensaje
        message.attach(body)

        #--------------------Archivo adjunto------------
        file="logo.png"

        with open(file, 'rb') as upload:
        #Leer como bytes
            #Crear contenido tipo base
            file_upload=MIMEBase("aplication", "octet-stream")
            #Ajuntar archivo
            file_upload.set_payload(upload.read())

        #Codificar archivo
        encode_base64(file_upload)

        #Aginar encabezado
        file_upload.add_header("Content-Disposition", f"attachment; filename={file}")
            
        #Generar conexión segura
        context=ssl.create_default_context()

        #Agregar contenido al mensaje
        message.attach(file_upload)

        try:

            #Generar conexión al servidor de gmail de manera segura
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as connection:
                
                #Iniciar sesión
                connection.login(self.email, self.password)
                print("Ha iniciado sesión a su cuenta de Gmail de manera segura")

                connection.sendmail(self.email, self.email_2, message.as_string())
                print("El mensaje ha sido enviado correctamente: ")

        except:

            print("Ocurrió un error al conectasre, verifique sus datos y la configuración de su cuenta de Gmail")


if __name__ == "__main__":

    send=send_email()



