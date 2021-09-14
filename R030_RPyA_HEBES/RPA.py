
import pyautogui as pag
import os
import time
import datetime
import glob
import keyboard
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta
from typing import NoReturn
from openpyxl import load_workbook
from time import sleep
import excel2sql
import webbrowser

def cleanUp():
    path = r"C:\Users\jpgarcia\Downloads\\" 
    downloads = glob.glob(path+"Detalle*.xlsx")
    for download in downloads:
        os.remove(download)
        print(download)

def encontrarPosImg():
    while True:
        posXY = pag.position()
        print(posXY, pag.pixel(posXY[0],posXY[1]))
        sleep(1)
        if  posXY[0] == 0:
            break

def encontrarImagen(rutaImagen,tiempo,confidence=.8): 
    TiempoIni=datetime.now()
    imagen=None	
    while (datetime.now()-TiempoIni).seconds<tiempo and imagen is None :
        time.sleep(0.3)
        try:
            imagen = pag.locateCenterOnScreen(rutaImagen, grayscale=True, confidence=confidence) 
        except: 
            continue
    time.sleep(0.3)    
    return imagen

def importarDetalleSelenium(): #Usando Selenium
    
    def generarRangoFecha():
        now = datetime.now()
        fechaPrevia = now - timedelta(days=60)
        fechaPrevia = fechaPrevia.strftime("%d/%m/%Y")
        fechaActual = now.strftime("%d/%m/%Y")
        rangofecha = str(fechaPrevia) +"  -  " + str(fechaActual)
        return rangofecha

    rangofecha = generarRangoFecha()
    user = 'aaguilera'
    pwd = 'Agosto2021'
    RUTA = r"C:\Users\jpgarcia\Documents\Visual Studio 2017\Python\chromedriver.exe" # Modificar w/ navDriver
    driver = webdriver.Chrome(RUTA)

    print("Iniciando Importación Dias"+ rangofecha) #Lanzar MM Zeus
    driver.get("https://funnel.mmtools.es/")
    driver.implicitly_wait(5)
    driver.delete_all_cookies()
    driver.maximize_window()
    sleep(2)
    usuario = driver.find_element_by_name("username").send_keys(user)
    sleep(1)
    pwd = driver.find_element_by_name("password").send_keys(pwd)
    sleep(1)
    loginBtn = driver.find_element_by_name("login-submit").click()
    sleep(1)
    loginBtn = driver.find_element_by_name("login-submit").click()
    sleep(1)
    driver.implicitly_wait(5)
    print('Login Terminado....')    #LogIn Terminado
    mostrarMasBtn = driver.find_element_by_xpath("/html/body/app-root/app-nav/div/app-funnel-sales/div/app-funnel-filter/app-box/div/div/div/button[1]").click()
    sleep(1)
    fechaBtn = driver.find_element_by_id("sell_date").clear()
    fechaBtn = driver.find_element_by_id("sell_date")
    fechaBtn.send_keys(rangofecha)
    sleep(1)
    keyboard.press_and_release('page down')
    sleep(2)
    multiBtn = driver.find_element_by_xpath("/html/body/app-root/app-nav/div/app-funnel-sales/div/app-funnel-filter/app-box/div/app-funnel-filter-expand/div/div[4]/div[7]/app-filter-form/div/app-multi-select/div/button").click()
    sleep(2)
    multiBtn = driver.find_element_by_xpath("/html/body/app-root/app-nav/div/app-funnel-sales/div/app-funnel-filter/app-box/div/app-funnel-filter-expand/div/div[4]/div[7]/app-filter-form/div/app-multi-select/div/div/div[4]").click()
    sleep(2)
    print('iniciando espera larga...')
    sleep(35)
    multiBtn = driver.find_element_by_xpath("/html/body/app-root/app-nav/div/app-funnel-sales/div/app-funnel-filter/app-box/div/app-funnel-filter-expand/div/div[4]/div[7]/app-filter-form/div/app-multi-select/div/button").click()
    print('Finalziada espera larga...')
    try:
        totalBtn1 = driver.find_element_by_xpath('//*[@id="funnel-table"]/tbody/tr[4]/td[2]/button').click()
        sleep(4)
    except:
        print("Error cliqueando en la cantidad de registros...")
        keyboard.press_and_release('page down')
        sleep(2)
    sleep(32)
    keyboard.press_and_release('page down')
    sleep(4)
    descargarBtn = driver.find_element_by_xpath("/html/body/app-root/app-nav/div/app-funnel-sales/div/app-funnel-detail/app-box/div/div[1]/div[2]/button[1]").click()
    sleep(75)
    driver.quit()

def importarDetallesCoordenadas(): #Usando Coordenadas:
    def abrirChrome():
        URL = 'https://funnel.mmtools.es/'
        keyboard.press_and_release('windows')
        sleep(1)
        keyboard.write('chrome')
        sleep(1)
        keyboard.press('enter')
        sleep(2)
        keyboard.write(URL)
        keyboard.press('enter')
        keyboard.press_and_release('windows+up')

    def iniciarExportacion():
        def generarRangoFecha():
            now = datetime.now()
            fechaPrevia = now - timedelta(days=1)
            fechaPrevia = fechaPrevia.strftime("%d/%m/%Y")
            fechaActual = now.strftime("%d/%m/%Y")
            rangofecha = str(fechaPrevia) +"  -  " + str(fechaActual)
            return rangofecha

        def expInsertarFecha():
            x,y = 215,312
            pag.moveTo(x,y, 0.5, pag.easeInQuad)
            pag.click(clicks=1, interval=0.25)
            sleep(1)
            keyboard.press_and_release('ctrl+a')
            rangofecha = generarRangoFecha()
            keyboard.write(rangofecha)
            sleep(1)
            keyboard.press('enter')

        print('Iniciado Importación...')
        x,y = 1013,576
        pag.moveTo(x,y, 2.5, pag.easeInQuad)
        pag.click(clicks=1, interval=0.25)
        sleep(5)
        x,y = 919,338
        pag.moveTo(x,y, 1.5, pag.easeInQuad)
        pag.click(clicks=1, interval=0.25)

        expInsertarFecha()

        x,y = 1089,898
        pag.moveTo(x,y, 0.5, pag.easeInQuad)
        pag.click(clicks=1, interval=0.25)
        sleep(5)

        x,y = 1089,928
        pag.moveTo(x,y, 0.5, pag.easeInQuad)
        pag.click(clicks=1, interval=0.25)
        sleep(2)
        keyboard.press_and_release('page down')

        x,y = 1040,277
        pag.moveTo(x,y, 1.5, pag.easeInQuad)
        pag.click(clicks=1, interval=0.25)
        sleep(12)

        x,y = 381,607
        pag.moveTo(x,y, 0.5, pag.easeInQuad)
        pag.click(clicks=1, interval=0.25)
        sleep(5)
        keyboard.press_and_release('page down')

        x,y = 1776,777
        pag.moveTo(x,y, 0.5, pag.easeInQuad)
        pag.click(clicks=1, interval=0.25)
        sleep(4.5)

        x,y = 1890,19
        pag.moveTo(x,y, 0.5, pag.easeInQuad)
        pag.click(clicks=1, interval=0.25)
        sleep(1.5)

def exportarDetalleSelenium():
    path = r"C:\Users\jpgarcia\Downloads\\" 
    downloads = glob.glob(path+"Detalle_*.xlsx")
    for downlaod in downloads:
        if "Detalle_" in downlaod:
            print(downlaod)
            print('Init Exportación del libro...')
            sleep(5)
            excel2sql.insertarExcel(downlaod)
    print('carterizando pronto...')        
    sleep(15)
    excel2sql.sql.execBBDD()
    webbrowser.open("http://caronte/ZEUS/vistas/automatizacion/automatizacion_hebe_clientes.php")