#TESTING GENERAR VALE MENU ALL FULL CHARGE ELEMENTS
#PYTHON VERSION : 3.11.2
#SELENIUM VERSION : 4.8.3
#NAVEGADOR : CHROME V 111.0.5563.65 (Build oficial) (64 bits)
#SCRIPT BY DARK MAU V 1.5
#IMPORTAR LIBRERIAS
import concurrent.futures #CONCURRENCIA Y PARALELISMO
import tkinter as tk #VENTANAS EMERGENTES
import keyboard #MANDAR ACCION DE TECLAS
import time #RETARDOS, FUNCION DE TIME
import os #INTERACCION DE SISTEMAIMP
import unittest #TEST DE PRUEBAS UNITARIAS
import openpyxl
#import actions
#FROMS PARA USAR FUNCIONES
#COMMON .PYTHON
import gspread
from common import*
from selenium.webdriver.support import expected_conditions as EC #EXPLICIT WAITS
from selenium.common.exceptions import NoSuchElementException #EXCEPTION para falla de encontrar elementos
from selenium.webdriver.support.ui import WebDriverWait #EXPLICIT WAITS
from selenium.common.exceptions import TimeoutException #USO DE TRY EXCEPT
from selenium.webdriver.chrome.options import Options #OPCIONES EXPERIMENTALES Y DE DESARROLLADOR
from selenium.webdriver.common.keys import Keys #USO DE ENVIO DE TECLAS
from selenium.webdriver.common.by import By #FUNCION BY PARA BUSQUEDA
from tkinter import simpledialog #DIALOGOS EN VENTANA EMERGENTE
from selenium import webdriver #IMPORTAR EL DRIVER DEL NAVEGADOR
#FIN DE IMPORTS
#DECLARACION DE VARIABLES DE TIEMPO
PAUSA = (10)
TIME = (1)
RETARD = (3)
URL = []
# Abrir IP en archivo Externo
ip = abrir_archivo_ip()
print("La IP encontrada es: ", ip)
#CLASS EMERGENT_WINDOW PARA USAR UNITTEST
class LOAD_GENERAR_VALE(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
#TEST 1 CORREO ERRONEO        
    def test_login1(self):
        driver = self.driver
        driver.get(ip)
        #CAMBIAR EL FRAME
        switch_to_frame(driver, "/html/frameset/frame", "FRAME 1")
        #EXPLICIT WAIT Y TRY CATCH        
        # BUSQUEDA Y LLENADO DE CAMPO DE CORREO ELECTRONICO
        xpath_email(driver, "//*[@id='ContentPlaceHolder1_txtCorreoElectronico']","marco.delgado@safi.unam.mx")
        #BUSQUEDA Y LLENADO DE CAMPO DE CONTRASEÑA
        xpath_password(driver,"//*[@id='ContentPlaceHolder1_txtContrasena']","897047")
        #BUSQUEDA Y CLICK DEL MENU DE VALE
        xpath_click(driver,"//*[@id='ContentPlaceHolder1_trvMenut2']")
        #CAMBIO DE FRAME A iFRAME
        switch_to_frame(driver,"/html/body/div[1]/div[2]/div/div/form/div[5]/iframe", "iFrame")
        #VERIFICAR LA CARGA DE ELEMENTOS CORRECTA
        diccionario_elementos = generar_diccionario_desde_excel()
        verificar_elementos(diccionario_elementos, driver)
    def tearDowm(self):
        driver = self.driver
        driver.close()
if __name__ == "__main__":
    unittest.main()
time.sleep(50)
self.driver.close
