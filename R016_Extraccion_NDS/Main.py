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
import AbrirMobility 
import subprocess
driver=None
Exito=AbrirMobility.AbrirMobility(driver)


while True : 
    today = datetime.today().strftime('%H%M')
    if int(today)>=800 and int(today)<=2240:
        print("--------------------------Empezar PROCESO---------------------------------")
        today = datetime.today().strftime('%d/%m/%Y')
        
        Exito=False
        while Exito!=True:
            print("------------Activacion-----------------")
            Exito=ProcesarCaso.ProcesarCaso('Activación','Activación',"http://ononetcanal/Mobility/Modules/Informes_Genericos/Informe.aspx?informe=TGT-A&toexcel=1&fechaDesde="+today+"&fechaHasta="+today,driver)
            if Exito==False:
                Exito=AbrirMobility.AbrirMobility(driver)
            print("------------Activacion FIN-----------------")
        
        Exito=False
        while Exito!=True:
            print("------------CIErre-----------------")
            Exito=ProcesarCaso.ProcesarCaso('Cierre','Cierre',"http://ononetcanal/Mobility/Modules/Informes_Genericos/Informe.aspx?informe=TGT-C&toexcel=1&fechaDesde="+today+"&fechaHasta="+today,driver)
            if Exito==False:
                Exito=AbrirMobility.AbrirMobility(driver)
            print("------------CIErre FIN-----------------")
        
        Exito=False
        while Exito!=True:
            print("------------Fallidas-----------------")
            Exito=ProcesarCaso.ProcesarCaso('Fallidas','Fallida',"http://ononetcanal/Mobility/Modules/ToExcel/ToExcelInformesFallidas.aspx?informe=F3&fechaDesde="+today+"&fechaHasta="+today+"&codCluster=0",driver)
            if Exito==False:
                Exito=AbrirMobility.AbrirMobility(driver)
            print("------------Fallidas FIN-----------------")
        
        Exito=False
        while Exito!=True:
            print("------------Bloqueos-----------------")
            Exito=ProcesarCaso.ProcesarCaso('Bloqueos','Bloqueo',"http://ononetcanal/Mobility/Modules/Informes_Genericos/Informe.aspx?informe=IBQ-CI&toexcel=1&fechaDesde="+today+"&fechaHasta="+today+"&codCluster=0",driver)
            if Exito==False:
                Exito=AbrirMobility.AbrirMobility(driver)
            print("------------Bloqueos FIN-----------------")
            
        print("Espero 120")
        time.sleep(60)
        print("Espero 120 OK")
    else:
        print("Espero HASTA MAÑANAAAAAA OK")
        
        Exito=AbrirMobility.Esperar(driver)
        time.sleep(180)
    
    






      