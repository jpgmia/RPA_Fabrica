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
import ProcesarCaso  

 
print("Click URL")
imagen=RPA.EncontrarImagen('resources\\images\\Mobility.png',30)
pag.click(imagen)
print("Click URL OK")


print("Poner URL") 
pag.write("funcionaaaaaaaaaaaaarar?", interval=0.05)      
print("Poner URL OK") 

 

pag.keyDown('ctrl')   
pag.press('a')  
pag.press('c')   
pag.keyUp('ctrl')

Leer=None
while   Leer is None :
    try:
        print("Copiar Clipboard")
        time.sleep(2)
        win32clipboard.OpenClipboard()
        Leer = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        print("Copiar Clipboard OK")
    except Exception as e: 
        print("Error  ---  Copiar Clipboard")
        continue
        
print(Leer)
