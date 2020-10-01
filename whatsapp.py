# ----------------------------------------------------------------------------
# Nombre:       WhatsApp.py
# Autor:        Gabriel F
# GitHub:       https://github.com/gab98fra/
# Creado:       01 de Octubre 2020
# Modificado:   01 de Octubre 2020
# Copyright:    (c) 2020 by Gabriel F, 2020
# ----------------------------------------------------------------------------


""" 
    Permite automatizar el envío de mensajes a través de WhatsApp

    python 3.8.1
    selenio 3.141.0

"""

# Para descargar geckodriver
# https://github.com/mozilla/geckodriver/releases



from selenium import webdriver
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.common.by import By
import time

class WhatsApp(object):

    def __init__(self):

        #Indicar path geckodriver
        self.browser=webdriver.Firefox(executable_path=r"C:\Users\user_one\Documents\Python\geckodriver.exe")
        self.browser.get('https://web.whatsapp.com/')

        #WebDriverWait(self.browser, 20)

        #Número de WhatsApp a enviar mensaje
        self.num="5556892390"
        #Mensaje
        self.mesagge="Hola amigo, este es un bot desde python con selenium, ¡NO Temas!"

        self.send()

    def send(self):

        self.browser.get("https://wa.me/{0}?text={1}".format(self.num, self.mesagge) )

        """
            Se debe escanear el QR con la app móvil

        """
        #Pausar 5 segundos  
        #time.sleep(5)
        
        #Botón contiuar
        self.browser.find_elements_by_xpath("//*[@id='action-button']")[0].click()

        #Botón usar WhatsApp Web
        button2=self.browser.find_elements_by_xpath("//*[@id='fallback_block/div/div/a']")[0]
        button2.click()
        

        #Botón enviar mensaje
        button3=self.browser.find_elements_by_xpath("//*[@id='main']/footer/div[1]/div[3]")[0]
        button3.click()
        time.sleep(3)

        #self.browser.quit()

        #Cerrar browser
        self.browser.close()



if __name__ == "__main__":

    message=WhatsApp()