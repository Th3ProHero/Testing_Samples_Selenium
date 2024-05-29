import concurrent.futures #CONCURRENCIA Y PARALELISMO
import tkinter as tk #VENTANAS EMERGENTES
import keyboard #MANDAR ACCION DE TECLAS
import time #RETARDOS, FUNCION DE TIME
import os #INTERACCION DE SISTEMAIMP
import unittest #TEST DE PRUEBAS UNITARIAS
import openpyxl
import gspread
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC #EXPLICIT WAITS
from selenium.common.exceptions import NoSuchElementException #EXCEPTION para falla de encontrar elementos
from selenium.webdriver.support.ui import WebDriverWait #EXPLICIT WAITS
from selenium.common.exceptions import TimeoutException #USO DE TRY EXCEPT
from selenium.webdriver.chrome.options import Options #OPCIONES EXPERIMENTALES Y DE DESARROLLADOR
from selenium.webdriver.common.keys import Keys #USO DE ENVIO DE TECLAS
from selenium.webdriver.common.by import By #FUNCION BY PARA BUSQUEDA
from tkinter import simpledialog #DIALOGOS EN VENTANA EMERGENTE
from selenium import webdriver #IMPORTAR EL DRIVER DEL NAVEGADOR

#ABRIR IP DESDE UN ARCHIVO EXTERNO TXT
def abrir_archivo_ip():
    dir_actual = os.path.dirname(os.path.abspath(__file__)) # Obtener la ruta actual
    ruta_archivo = os.path.join(dir_actual, "IPSIVALE.txt") # Indicar el nombre del archivo de texto con la IP
    archivo = open(ruta_archivo, "r") # Abrir el archivo de texto
    contenido = archivo.readlines() # Leer el contenido del archivo
    ip = " ".join(contenido) # Convertir el contenido en una cadena con la IP
    archivo.close() # Cerrar el archivo
    return ip

#BUSQUEDA Y LLENADO DE CAMPOS POR XPATH
def xpath_email(driver, xpath_email, valor_email):
    try:
        elementEmail = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, xpath_email)))
        elementEmail.send_keys(valor_email)
    except TimeoutException as ex:
        print(ex)
        print(f"El elemento EMAIL con xpath {xpath} no está disponible")
        
#CAMPOS DE CONTRASEÑA LLENADO & ENTER
def xpath_password(driver, xpath_pass, valor_pass):
    try:
        elementPassword = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, xpath_pass)))
        elementPassword.send_keys(valor_pass)
        elementPassword.send_keys(Keys.ENTER)
    except TimeoutException as ex:
        print(ex)
        print(f"El elemento PASSWORD con xpath {xpath} no está disponible")

#LOGIN FUNCTION AMBOS CAMPOS


#LLENAR UN CAMPO CON TEXTO
def xpath_insert_text(driver, xpath_Text, valor_Text):
    try:
        elementText = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, xpath_Text)))
        elementText.send_keys(valor_Text)
        #elementText.send_keys(Keys.ENTER)
    except TimeoutException as ex:
        print(ex)
        print(f"El elemento para insertar Texto con xpath {xpath} no está disponible")        
        
#BUSQUEDA DE ELEMENTO + CLICK
def xpath_click(driver, xpath_ck):
    try:
        elementClick = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, xpath_ck)))
        elementClick.click()
    except TimeoutException as ex:
        print(ex)
        print(f"El elemento CLICK con xpath {xpath_ck} no está disponible")
        
#CAMBIO DE FRAME        
def switch_to_frame(driver, xpath_frame, nombre):
    try:
        frame = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, xpath_frame)))
        driver.switch_to.frame(frame)
        print(f"Se ha cambiado al frame '{nombre}' exitosamente.")
    except TimeoutException as ex:
        print(ex)
        print(f"No se pudo cambiar al frame con el xpath {xpath_frame}.")
        
#Utilizar datos de excel local
def generar_diccionario_desde_excel():
    # Ruta del archivo .xlsx
    archivo = "elements.xlsx"

    # Cargar el archivo .xlsx
    libro = openpyxl.load_workbook(archivo)

    # Seleccionar la hoja de trabajo (worksheet)
    hoja = libro.active

    # Crear el diccionario
    elementos = {}

    # Obtener los valores de las columnas A y B, ignorando la primera celda
    for fila in hoja.iter_rows(min_row=2, values_only=True):
        columna_a = fila[0]
        columna_b = fila[1]
        elementos[columna_a] = columna_b

    # Cerrar el archivo
    libro.close()

    # Retornar el diccionario generado
    return elementos

#FUNCION PARA RECORRER EL DICCIONARIO
def verificar_elementos(elementos, driver):
    for nombre, xpath in elementos.items():
        try:
            elemento = driver.find_element("xpath", xpath)
            print(f"Elemento cargado correctamente: {nombre}")
        except NoSuchElementException:
            print(f"Elemento no encontrado: {nombre}")
            
#OBTENER TEXTO DE UN XPATH
def obtener_texto_elemento(nombre_xpath, xpath):
    # Inicializar el controlador del navegador (por ejemplo, Chrome)
    driver = webdriver.Chrome()

    try:
        # Encontrar el elemento mediante el XPath
        elemento = driver.find_element_by_xpath(xpath)
        # Obtener el texto del elemento
        contenido = elemento.text
        # Imprimir el resultado
        print(f"El contenido del elemento {nombre_xpath} es: {contenido}")
    except NoSuchElementException:
        # Imprimir el mensaje de elemento no disponible
        print("El elemento no está disponible")

# Subir archivos a un apartado.

def subir_archivo(nombre, xpath, ruta_archivo):
    try:
        driver = webdriver.Chrome()  # Aquí debes usar el driver adecuado para tu navegador
        driver.get("URL_DE_LA_PAGINA")  # Reemplaza "URL_DE_LA_PAGINA" por la URL del sitio web donde deseas subir el archivo
        
        # Encuentra el botón o campo de carga de archivos utilizando el xpath proporcionado
        elemento_carga = driver.find_element_by_xpath(xpath)
        
        # Envía la ruta del archivo al botón o campo de carga
        elemento_carga.send_keys(ruta_archivo)
        
        print(f"El archivo '{nombre}' pudo subirse con éxito.")
        
    except Exception as e:
        print(f"Error al subir el archivo '{nombre}': {str(e)}")

# Maquinas virtuales

