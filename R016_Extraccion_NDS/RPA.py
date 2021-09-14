 
 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui as pag
from datetime import datetime
#pyautogui.hotkey('ctrl', 'c')
import win32clipboard
import time
import openpyxl
import os
import psutil
import subprocess

pag.FAILSAFE = False

        
def CerrarCitrix(): 
    for proc in psutil.process_iter():
        if proc.name() == "concentr.exe" or proc.name() == "Receiver.exe" or proc.name() == "SelfServicePlugin.exe" or proc.name() == "wfcrun32.exe" :
            a=None
            proc.kill()
    time.sleep(2)
    a=subprocess.Popen(["C:\Program Files (x86)\Citrix\ICA Client\SelfServicePlugin\SelfService.exe", ""])
    time.sleep(2)
    
def EncontrarImagen(rutaImagen,tiempo,confidence=.9): 
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
    
    
def EncontrarElementoByName(driver,name,tiempo): 
    TiempoIni=datetime.now()
    elem=None	
    while (datetime.now()-TiempoIni).seconds<tiempo and elem is None :
        time.sleep(0.3)
        try:
            elem = driver.find_element_by_name(name)
        except: 
            continue
    time.sleep(0.3)    
    return elem   

def EncontrarElementoById(driver,name,tiempo): 
    TiempoIni=datetime.now()
    elem=None	
    while (datetime.now()-TiempoIni).seconds<tiempo and elem is None :
        time.sleep(0.3)
        try:
            elem = driver.find_element_by_id(name)
        except: 
            continue
    time.sleep(0.3)    
    return elem     
    
    
def EncontrarElementoByText(driver,name,tiempo): 
    TiempoIni=datetime.now()
    elem=None	
    while (datetime.now()-TiempoIni).seconds<tiempo and elem is None :
        time.sleep(0.3)
        try:
            elem = driver.find_element_by_link_text(name)
        except: 
            continue
    time.sleep(0.3)    
    return elem  

def EncontrarElementoByClass(driver,name,tiempo): 
    TiempoIni=datetime.now()
    elem=None	
    while (datetime.now()-TiempoIni).seconds<tiempo and elem is None :
        time.sleep(0.3)
        try:
            elem = driver.find_element_by_class_name(name)
        except: 
            continue
    time.sleep(0.3)    
    return elem     




    
    
def AbrirChrome(URL): 
    driver = webdriver.Chrome("resources\\chrome\\chromedriver.exe")
    driver.get(URL)    
    return driver  