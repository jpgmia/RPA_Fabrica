import pyautogui as pag
import os
import time
import datetime
import glob
import keyboard
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from datetime import datetime, timedelta
from typing import NoReturn
from openpyxl import load_workbook
import sql

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

def cleanUp():
    path = r"C:\Users\jpgarcia\Downloads\\" 
    downloads = glob.glob(path+"*Corte Automatizado*.xlsx")
    for download in downloads:
        os.remove(download)
        print(download)

def importarCorteSelenium(): #Usando Selenium  Keystrokes & coordenadas
    URL = 'https://apps.mypurecloud.de/directory/#/engage/reports/new'
    URLDescargas = 'https://apps.mypurecloud.de/directory/#/engage/reports'
    RUTA = r"C:\Users\jpgarcia\Documents\Visual Studio 2017\Python\chromedriver.exe" # Modificar w/ navDriver
    driver = webdriver.Chrome(RUTA)
    user = 'beatriz.rodriguez.cases@callcenter.masmovil.com'
    pwd = 'nm8xkDoq'
    driver.get(URL)
    driver.implicitly_wait(5)
    driver.delete_all_cookies()
    driver.maximize_window()
    print("Iniciando Importación Dias"+ str(datetime.now())) #Lanzar MM Zeus

    def LogIn():
        sleep(2)
        usuario = driver.find_element_by_id("email").send_keys(user)
        sleep(1)
        passw = driver.find_element_by_id("password").send_keys(pwd)
        sleep(1)
        loginBtn = driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div[1]/div[2]/div/div[1]/div/form/button").click()
        sleep(5)
        driver.implicitly_wait(5)
        print('Login Terminado....')    #LogIn Terminado
        driver.implicitly_wait(5)
        sleep(4)
 
    def buscarYposicionar(buscar):
        keyboard.press_and_release('ctrl+f')
        sleep(1)
        keyboard.write(buscar)
        sleep(1)
        keyboard.press('esc')
        sleep(1)
        keyboard.press('tab')
        sleep(1)

    LogIn()

    x,y = 454,211
    pag.moveTo(x,y, 1.5, pag.easeInQuad)
    pag.click(clicks=1, interval=0.25)
    sleep(5)

    x,y = 930,563
    pag.moveTo(x,y, 0.5, pag.easeInQuad)
    pag.click(clicks=1, interval=0.25)
    sleep(5)

    buscar = 'Nombre Informe'
    now = datetime.now()
    fechaActual = now.strftime("%d-%m-%Y-%H%M%S")
    fechaActual = str(fechaActual)
    nombreinforme = 'Ejemplo Corte Automatizado' + fechaActual
    buscarYposicionar(buscar)
    keyboard.write(nombreinforme)
    keyboard.press('enter')

    buscar = 'Formato de archivo del informe'
    buscarYposicionar(buscar)
    keyboard.write(buscar)
    keyboard.press('right')
    keyboard.press('right')
    sleep(1)
    keyboard.press('right')
    keyboard.press('enter')

    informes = ["Q_VZ_MASMOVIL_MK_RES_ATC_ATC","Q_VZ_MASMOVIL_MK_RES_ATC_ATC_CATALAN","Q_VZ_MASMOVIL_MK_RES_ATC_AVERIAS_FIJO","Q_VZ_MASMOVIL_MK_RES_ATC_AVERIAS_MOVIL","Q_VZ_MASMOVIL_MK_RES_ATC_AVERIAS_TELEVISION"]
    informess = ["Q_VZ_MASMOVIL_MK_RES_ATC_ATC"]

    buscar = 'Cola(s)'

    buscarYposicionar(buscar)

    for informe in informes:
        print(informe)
        sleep(1)
        keyboard.write(informe,delay=0.009)
        sleep(1)
        keyboard.press('enter')
        keyboard.press('enter')
        sleep(1)

    buscar = 'Configuración regional del informe'
    buscarYposicionar(buscar)
    keyboard.write('Español')
    keyboard.press('enter')

    buscar = 'Período'
    buscarYposicionar(buscar)
    keyboard.write('Ayer')
    keyboard.press('enter')

    buscar = 'Zona horaria'
    buscarYposicionar(buscar)
    keyboard.write('Europa/Madrid')
    keyboard.press('enter')
    sleep(1)

    keyboard.press_and_release('ctrl+f')
    sleep(1)
    keyboard.write("Guardar")
    sleep(1)
    keyboard.press('esc')

    x,y = 153,952
    pag.moveTo(x,y, 0.5, pag.easeInQuad)
    pag.doubleClick()
    sleep(3)
    pag.click(clicks=1, interval=0.25)
    sleep(3)

    x,y = 134,435
    pag.moveTo(x,y, 0.5, pag.easeInQuad)
    pag.click(clicks=1, interval=1.25)
    sleep(3)

    x,y = 469,329
    pag.moveTo(x,y, 0.5, pag.easeInQuad)
    pag.click(clicks=1, interval=1.25)
    sleep(2)
    driver.refresh()
    driver.implicitly_wait(5)
    driver.quit()
    print('iniciando de nuevo')

    driver = webdriver.Chrome(RUTA)
    driver.get(URLDescargas)
    driver.implicitly_wait(5)
    driver.delete_all_cookies()
    driver.maximize_window()

    LogIn()
    sleep(3)

    x,y = 454,211
    pag.moveTo(x,y, 1.5, pag.easeInQuad)
    pag.click(clicks=1, interval=0.25)
    sleep(5)
    keyboard.press_and_release('ctrl+f')
    sleep(1)
    keyboard.write("XLSX")
    sleep(1)
    keyboard.press('esc')
    sleep(1)
    keyboard.press('enter')
    sleep(2)
    keyboard.press_and_release('enter')
    print("buscado y posicionado")
    sleep(12)
    driver.quit()

def generarFichero():
    getQuery = r"SELECT 'MASMOVIL ATC' as SKILL, concat(concat(SUBSTRING(fecha,0,7),'20'),SUBSTRING(fecha,7,2)) as FECHA ,CASE WHEN LEN(Intervalo)=4 THEN CONCAT('0',Intervalo) ELSE Intervalo END AS FRANJA ,SUBSTRING(Ofrecidas,0,  CHARINDEX('.', Ofrecidas)) AS VOL_ENTRANTES ,SUBSTRING(contestadas,0,  CHARINDEX('.', contestadas)) AS VOL_CONTESTADAS ,'' VOL_CONTESTADAS_NDS, case when [AHT]='N/A' then '0' else DATEDIFF(SECOND,0,AHT)/60  end AS TMO, '' AS NDS, CASE WHEN CAST(contestadas AS NUMERIC)<>0 AND CAST(Ofrecidas AS NUMERIC)<>0 THEN ROUND((CAST(contestadas AS FLOAT)/CAST(Ofrecidas AS FLOAT)*100),2) ELSE 0 END NAT FROM [RPyA].[dbo].[RPyA_2MARES]"
    keyboard.press_and_release('windows')
    sleep(1)
    keyboard.write('Template2Mar')
    sleep(2)
    keyboard.press('enter')
    sleep(5)
    keyboard.press_and_release('windows+up')
    sleep(1)
    keyboard.press_and_release('alt')
    sleep(1)
    keyboard.press_and_release('d')
    sleep(1)
    keyboard.write('pn')
    sleep(1)
    keyboard.press_and_release('b')
    sleep(1)
    keyboard.press_and_release('s')
    sleep(5)
    keyboard.press('tab')
    sleep(1)
    keyboard.press('enter')
    keyboard.press_and_release('enter')
    sleep(5)
    keyboard.write('MKTCRM')
    keyboard.press('tab')
    sleep(1)
    keyboard.write('RPyA')
    sleep(1)
    keyboard.press('tab')
    pag.moveTo(625,559, 0.5, pag.easeInQuad)
    pag.click(clicks=1, interval=0.25)
    sleep(2)
    keyboard.press('tab')
    sleep(1)
    keyboard.press('tab')
    keyboard.write(getQuery)
    keyboard.press('tab')
    sleep(1)
    keyboard.press('tab')
    sleep(1)
    keyboard.press('tab')
    sleep(1)
    keyboard.press('tab')
    sleep(1)
    keyboard.press('enter')
    sleep(5)
    keyboard.press('enter')
    sleep(2)
    pag.moveTo(227,988, 0.5, pag.easeInQuad)
    pag.click(button='right', clicks=3, interval=0.25)
    sleep(1)
    keyboard.write('e')
    sleep(1)
    pag.moveTo(197,988, 0.5, pag.easeInQuad)
    pag.click(button='right', clicks=3, interval=0.25)
    sleep(2)
    keyboard.write('c')
    sleep(2)
    now = datetime.now()
    fechaActual = now.strftime("%Y%d%m_%H%M%S")
    nombre = f"{fechaActual}_Historico_KPIs"
    keyboard.write(nombre)
    keyboard.press('enter')
    keyboard.press_and_release('F12')
    sleep(10)
    keyboard.write(nombre)
    sleep(2)
    keyboard.press('tab')
    sleep(2)
    keyboard.write('comma')
    sleep(5)
    keyboard.press_and_release('alt+g')