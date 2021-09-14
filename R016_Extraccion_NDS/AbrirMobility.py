from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui as pag
from datetime import datetime
#pyautogui.hotkey('ctrl', 'c')
import win32clipboard
import time
import openpyxl
import os
import RPA 
import re

from openpyxl.cell.cell import ILLEGAL_CHARACTERS_RE

def AbrirMobility(driver): 

    pag.FAILSAFE = False
    print("Cerrar Excel 1")
    imagen=RPA.EncontrarImagen('resources\\images\\CerrarExcel.png',2) 
    print("2")   
    if imagen is not None:
        pag.click(imagen)
    print("3")   
    print("Cerrar Excel 1 OK")
    
    print("Cerrar Excel 2")
    imagen=RPA.EncontrarImagen('resources\\images\\CerrarExcel2.png',2)
    if imagen is not None:    
        pag.click(imagen)
    print("Cerrar Excel 2 OK")
    
    #imagen=RPA.EncontrarImagen('resources\\images\\CerrarMobility2.png',2)   
    #if imagen is not None: 
    #    pag.click(imagen)

    imagen=RPA.EncontrarImagen('resources\\images\\CerrarMobility3.png',2) 
    if imagen is not None: 
        pag.click(imagen)
        
    #imagen=RPA.EncontrarImagen('resources\\images\\CerrarMobility5.png',2) 
    #if imagen is not None: 
    #    pag.click(imagen)
        
    if driver is not None: 
        driver.close()
        driver.quit()
    
    print("Inicio")

    print("CerrarCitrix")
    RPA.CerrarCitrix()
    print("CerrarCitrix OK")

    #Minimizar consola           
    #start=RPA.EncontrarImagen('resources\\images\\Console.png',30)
    #pag.doubleClick(start)
    #print("Minimizar consola")

        
    #Abrir chrome 
    print("Abrir chrome")
    driver=RPA.AbrirChrome("https://distribucion.vodafone.es/")
    print("Abrir chrome OK")
     
    #Poner usuario
    print("Poner Usuario")
    elem=RPA.EncontrarElementoByName(driver,"username",30)
    elem.send_keys("nlealpe1")
    print("Poner Usuario OK")


    #Poner Contraseña 
    print("Poner Contraseña") 
    elem=RPA.EncontrarElementoByName(driver,"password",30)
    elem.send_keys("2021Marzo.")
    print("Poner Contraseña OK")

    #Click login
    print("Click Login")
    elem=RPA.EncontrarElementoByName(driver,"submit",30)
    elem.click()
    print("Click Login OK")

    #Click detectar cotrix
    print("Click Detectar")
    elem=RPA.EncontrarElementoById(driver,"protocolhandler-welcome-installButton",30)
    time.sleep(1)
    elem.click()
    print("Click Detectar OK")

    #Click prmitir
    print("Click Check")
    start=RPA.EncontrarImagen('resources\\images\\CheckCitrix.png',30)
    pag.click(start)
    print("Click Check OK")

     #Click abrir
    print("Click Abrir")
    start=RPA.EncontrarImagen('resources\\images\\AbiriCitrix.png',30)
    pag.click(start)  
    print("Click Abrir OK")
          
     
    #Click Mobility  
    print("Minimizo chrome")
    driver.minimize_window()    
    print("Minimizo chrome OK")

    #Click URL
    print("------------Abrir Mobility-----------------")
    elem=RPA.EncontrarElementoByText(driver,"IExplorer_IE11",30)
    imagen=None
    while imagen==None :
        while True:
            try:
                elem.click()
                print("click Mobility OK")
                break
            except:
                try:
                    print("Error -  click mobility")
                    driver.get("https://distribucion.vodafone.es/");
                    print("Refresh Chrome")
                    elem=RPA.EncontrarElementoByText(driver,"IExplorer_IE11",10)
                    continue
                except Exception as e: 
                    print(e)
                    print("Error - Refresh Chrome")
                    continue
                continue
        print("Busco File")      
        imagen=RPA.EncontrarImagen('resources\\images\\FileMobility.png',120)
        print("FIN Busco File")
        
    print("------------Abrir Mobility OK-----------------")

    print("Clicks File")
    pag.click(imagen)
    print("Clicks File OK")


    print("Nueva Pestaña")
    imagen=RPA.EncontrarImagen('resources\\images\\NuevaTestania.png',5)
    pag.click(imagen)
    print("Nueva Pestaña OK")

    print("Esperar New TAB")
    start=RPA.EncontrarImagen('resources\\images\\NewTab.png',120)
    print("Esperar New OK")
        
    print("Click URL")
    imagen=RPA.EncontrarImagen('resources\\images\\Mobility.png',30)
    pag.click(imagen)
    print("Click URL OK")
     
       
    print("Poner URL")
    URL="http://ononetcanal/Mobility"
    pag.write(URL, interval=0.05)
    print("Poner URL OK")	
     
     #Ir URL
    print("IR URL")
    start=RPA.EncontrarImagen('resources\\images\\IrMobility.png',30)
    pag.doubleClick(start) 
    print("Ir URL OK")

    print("Esperar ONO")
    start=RPA.EncontrarImagen('resources\\images\\Ono.png',180)
    print("Esperar ONO OK")

    print("Minimizar ONO")
    start=RPA.EncontrarImagen('resources\\images\\MinMobility.png',30)
    pag.click(start) 
    print("Minimizar ONO OK")
    
    return True;
    
    
    
    
def Esperar(driver): 

    pag.FAILSAFE = False
    print("Cerrar Excel 1")
    imagen=RPA.EncontrarImagen('resources\\images\\CerrarExcel.png',2) 
    print("2")   
    if imagen is not None:
        pag.click(imagen)
    print("3")   
    print("Cerrar Excel 1 OK")
    
    print("Cerrar Excel 2")
    imagen=RPA.EncontrarImagen('resources\\images\\CerrarExcel2.png',2)
    if imagen is not None:    
        pag.click(imagen)
    print("Cerrar Excel 2 OK")
    
    imagen=RPA.EncontrarImagen('resources\\images\\CerrarMobility2.png',2)   
    if imagen is not None: 
        pag.click(imagen)

    imagen=RPA.EncontrarImagen('resources\\images\\CerrarMobility3.png',2) 
    if imagen is not None: 
        pag.click(imagen)
    if driver is not None: 
        driver.close()
        driver.quit()
    
    print("Inicio")

    print("CerrarCitrix")
    RPA.CerrarCitrix()
    print("CerrarCitrix OK")

    #Minimizar consola           
    #start=RPA.EncontrarImagen('resources\\images\\Console.png',30)
    #pag.doubleClick(start)
    #print("Minimizar consola")

        
    #Abrir chrome 
    print("Abrir chrome")
    driver=RPA.AbrirChrome("https://distribucion.vodafone.es/")
    print("Abrir chrome OK")
     
    
    return True;    