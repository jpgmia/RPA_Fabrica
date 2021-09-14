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

def ProcesarCaso(nombreExcel,nombreCarpeta,URL,driver): 
    
    time.sleep(5)
    
    #Click Mobility 

    print("Clicks File")    
    imagen=RPA.EncontrarImagen('resources\\images\\FileMobility.png',30)
    pag.click(imagen)
    print("Clicks File OK")
    
    print("Nueva Pestaña")
    imagen=RPA.EncontrarImagen('resources\\images\\NuevaTestania.png',5)
    pag.click(imagen)
    print("Nueva Pestaña OK")
    
    print("Esperar New TAB")
    start=RPA.EncontrarImagen('resources\\images\\NewTab.png',120)
    print("Esperar New OK")
    
    if start is None:
        return False 
        
            

    
    
        
    Leer=None;
    while Leer!=URL:
    
        imagen=RPA.EncontrarImagen('resources\\images\\Mobility.png',30)
        pag.click(imagen)
        if imagen is None:
            return False 
        print("Click URL OK")

        
        print("Poner URL") 
        pag.write(URL, interval=0.05)      
        print("Poner URL OK") 
        
        
        
        Leer=None;
        
            
       

        TiempoIni=datetime.now()
        while (datetime.now()-TiempoIni).seconds<30 and Leer is None :
            try:
                win32clipboard.OpenClipboard()
                win32clipboard.EmptyClipboard()
                win32clipboard.CloseClipboard()
                pag.keyDown('ctrl')   
                pag.press('a')  
                pag.press('c')   
                pag.keyUp('ctrl')
                print("Copiar Clipboard")
                time.sleep(2)
                win32clipboard.OpenClipboard()
                Leer = win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)
                win32clipboard.CloseClipboard()
                print("Copiar Clipboard OK")
            except Exception as e: 
                print("Error  ---  Copiar Clipboard: ")
                print(e)
                continue
        print(Leer)
        print(URL)        
    
    print("IR URL")
    imagen=RPA.EncontrarImagen('resources\\images\\IrMobility.png',5)
    if imagen is None:
        print("ERROR --- IR URL")
        
        return False  
        
    pag.doubleClick(imagen)
    print("IR URL OK")
   
    print("OPEN Excel")
    imagen=RPA.EncontrarImagen('resources\\images\\Open.png',60) 
    if imagen is None:
        return False
        
        
    time.sleep(0.5)
    pag.doubleClick(imagen)
    print("OPEN Excel OK")
    
    print("OPEN SI Excel")
    imagen=RPA.EncontrarImagen('resources\\images\\SiExcel.png',60) 
    if imagen is None:
        print("ERROR - OPEN SI Excel")
        return False
    pag.click(imagen)  
    print("OPEN SI Excel OK")
    
    print("Click todo Excel")
    imagen=RPA.EncontrarImagen('resources\\images\\todoExcel.png',60) 
    pag.moveTo(imagen)
    pag.click(button='right')
    print("Click todo Excel OK")
     
      
    
    print("Copiar Excel")
    imagen=RPA.EncontrarImagen('resources\\images\\CopyExcel.png',60) 
    pag.doubleClick(imagen)     
    print("Copiar Excel OK")

            
    Activavion=None
    while   Activavion is None :
        try:
            print("Copiar Clipboard")
            time.sleep(2)
            win32clipboard.OpenClipboard()
            Activavion = win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)
            win32clipboard.CloseClipboard()
            print("Copiar Clipboard OK")
        except Exception as e: 
            print("Error  ---  Copiar Clipboard")
            continue
    
    print("Cerrar Excel 1")
    imagen=RPA.EncontrarImagen('resources\\images\\CerrarExcel.png',5)   
    pag.click(imagen)
    print("Cerrar Excel 1 OK")
    
    print("Cerrar Excel 2")
    imagen=RPA.EncontrarImagen('resources\\images\\CerrarExcel2.png',5)   
    pag.click(imagen)
    print("Cerrar Excel 2 OK")
    
     
     
    
    print("Clicks File")
    imagen=RPA.EncontrarImagen('resources\\images\\FileMobility.png',30)
    pag.click(imagen)
    print("Clicks File OK")
    
    print("Cerrar Pestaña")
    imagen=RPA.EncontrarImagen('resources\\images\\CerrarPestania.png',30,confidence=.7)
    pag.click(imagen)
    print("Cerrar Pestaña OK")
    
    #imagen=RPA.EncontrarImagen('resources\\images\\CerrarMobility.png',5)   
    #pag.click(imagen)
    #imagen=RPA.EncontrarImagen('resources\\images\\CerrarMobility.png',2)   
    #pag.click(imagen)
    #imagen=RPA.EncontrarImagen('resources\\images\\CerrarMobility4.png',2)   
    #pag.click(imagen)
    
    print("GUARDAR EXCEL")
  
    
    
    filas=Activavion.split("\n")

    excel_document = openpyxl.load_workbook('resources\\excel\\'+nombreExcel+'.xlsx')
    sheet = excel_document['Hoja1']
    for indice in range(0,len(filas)):
        celdas=filas[indice].split("\t")
        for comunla in range(0,len(celdas)):
            sheet.cell(column=comunla+1, row=indice+1, value="{0}".format(ILLEGAL_CHARACTERS_RE.sub(r'', celdas[comunla])))
            
            
    

    
    contenido = os.listdir('\\\\172.21.0.200\\operaciones\\POWERBI\\PRODUCCION\\VDF_EXTRACCION_NDS\\'+nombreCarpeta+'')
    ruta='\\\\172.21.0.200\\operaciones\\POWERBI\\PRODUCCION\\VDF_EXTRACCION_NDS\\'+nombreCarpeta+'\\'
    today = datetime.today().strftime('%Y-%m-%d')
    for archivo in contenido:
        if archivo.find(nombreExcel+"-"+today) != -1:
            os.remove(ruta+archivo)

    
    today = datetime.today().strftime('%Y-%m-%d')
    excel_document.save('\\\\172.21.0.200\\operaciones\\POWERBI\\PRODUCCION\\VDF_EXTRACCION_NDS\\'+nombreCarpeta+'\\'+nombreExcel+'-'+today+'.xlsx')
    print("GUARDAR EXCEL OK")
    
    return True;