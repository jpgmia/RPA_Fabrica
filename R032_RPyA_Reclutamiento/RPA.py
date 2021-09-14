
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

def ExtraerInforme(): #Usando Selenium
    now = datetime.now()
    fechaActual = now.strftime("%d-%m-%Y")
    nombrefichero = "Reporte Automatizado " + fechaActual
    user = 'automatizaciones@mia.as'
    pwd = 'RPAautomatizaciones21'
    RUTA = r"C:\Users\jpgarcia\Documents\Visual Studio 2017\Python\chromedriver.exe" # Modificar w/ navDriver
    driver = webdriver.Chrome(RUTA)

    print("Iniciando Importación Dias"+ fechaActual) #Lanzar MM Zeus
    driver.get("https://console.33bot.io/#/login/login")
    driver.implicitly_wait(5)
    driver.delete_all_cookies()
    driver.maximize_window()
    sleep(2)
    usuario = driver.find_element_by_xpath("/html/body/app-root/app-login/div/div[1]/div[2]/div/div[3]/div[1]/input").send_keys(user)
    sleep(1)
    pwd = driver.find_element_by_xpath("/html/body/app-root/app-login/div/div[1]/div[2]/div/div[3]/div[2]/input").send_keys(pwd)
    sleep(1)
    loginChk = driver.find_element_by_xpath('//*[@id="mat-checkbox-1"]/label/div').click()
    sleep(1)
    loginBtn = driver.find_element_by_xpath("/html/body/app-root/app-login/div/div[1]/div[2]/div/div[5]/button").click()
    sleep(1)
    verMasBtn = driver.find_element_by_xpath("/html/body/ion-app/ng-component/div/main-menu/nav/div[5]").click()
    sleep(1)
    usuarioabuscar = driver.find_element_by_xpath("/html/body/ion-app/ng-component/div/ion-nav/page-sys-admin-change-session/ion-content/div[2]/div/div/div[3]/div/div/ion-item/div[1]/div/ion-input/input").send_keys("diego.gonzalezf.90@gmail.com")
    sleep(2)
    usuarioclick = driver.find_element_by_xpath("/html/body/ion-app/ng-component/div/ion-nav/page-sys-admin-change-session/ion-content/div[2]/div/div/div[3]/div/table/tbody/tr/td[1]").click()
    sleep(1)
    driver.implicitly_wait(5)
    print('Login Terminado....')    #LogIn Terminado
    sleep(3)
    driver.implicitly_wait(5)
    marktelReclutamiento = driver.find_element_by_xpath("/html/body/ion-app/ng-component/div/ion-nav/page-chats/ion-content/div[2]/div/div/ion-row[2]/ion-col[4]/ion-card/ion-card-content/ion-row/ion-col[2]/div/h2").click()
    sleep(1)
    estadisticasBtn = driver.find_element_by_xpath("/html/body/ion-app/ng-component/div/secondary-menu/nav/div[3]/div[2]/div[4]/div[1]").click()
    sleep(1)
    estadisticasDatosBtn = driver.find_element_by_xpath("/html/body/ion-app/ng-component/div/secondary-menu/nav/div[3]/div[2]/div[4]/div[2]/div/div[3]/div").click()
    driver.implicitly_wait(5)
    sleep(5)
    nuevoInformeBtn = driver.find_element_by_xpath("/html/body/ion-app/ng-component/div/ion-nav/chat-group-report-list-page/ion-content/div[2]/div/div/ion-row/ion-col[2]/button").click()
    sleep(2)
    nombrenuevoInforme = driver.find_element_by_xpath("/html/body/ion-app/ng-component/div/ion-nav/chat-group-report-list-page/ion-content/div[1]/div/div[3]/div/div/ion-content/div[2]/div[3]/div/ion-input/input").send_keys(nombrefichero)
    sleep(3)
    sesionuevoInformeBtn = driver.find_element_by_xpath("/html/body/ion-app/ng-component/div/ion-nav/chat-group-report-list-page/ion-content/div[1]/div/div[3]/div/div/ion-content/div[2]/div[5]/ng-select/div/input").click()
    sleep(3)
    sesionuevoInformeBtn = driver.find_element_by_xpath("/html/body/ion-app/ng-component/div/ion-nav/chat-group-report-list-page/ion-content/div[1]/div/div[3]/div/div/ion-content/div[2]/div[5]/ng-select/div/input").send_keys("Import all")
    sleep(3)
    pag.press('enter')
    sleep(5)
    variablesglonuevoInformeBtnn = driver.find_element_by_xpath("/html/body/ion-app/ng-component/div/ion-nav/chat-group-report-list-page/ion-content/div[1]/div/div[3]/div/div/ion-content/div[2]/div[7]/ng-select/div/input").click()
    sleep(5)
    variablesglonuevoInformeBtn = driver.find_element_by_xpath("/html/body/ion-app/ng-component/div/ion-nav/chat-group-report-list-page/ion-content/div[1]/div/div[3]/div/div/ion-content/div[2]/div[7]/ng-select/div/input").send_keys("Import all")
    sleep(4)
    pag.press('enter')
    nuevoInformeBtn = driver.find_element_by_xpath("/html/body/ion-app/ng-component/div/ion-nav/chat-group-report-list-page/ion-content/div[1]/div/div[3]/div/div/ion-content/div[2]/div[7]/ng-select/div/span/span[20]/span/a").click()
    sleep(2)
    nuevoInformeBtn = driver.find_element_by_xpath("/html/body/ion-app/ng-component/div/ion-nav/chat-group-report-list-page/ion-content/div[2]/div/div/ion-row/ion-col[2]/button").click()
    sleep(2)