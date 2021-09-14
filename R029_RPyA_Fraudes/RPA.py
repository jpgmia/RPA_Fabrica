import keyboard
import pyautogui as pt 
from datetime import datetime
import pyperclip
import socket
import time
import pyodbc
import os

r = ()
tabla = []
resultado = ()
chromePath = "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"

TiempoInicial=str(datetime.now())


print('Iniciando script de fraudes a las ...' + TiempoInicial)


def cleanUp():
    try:
        os.system("taskkill /im chrome.exe /f")
    except:
        print('Chrome No Esta Abierto')

def abrirChrome():
    global x, y
    x, y = 58, 40
    keyboard.press_and_release('windows+m')
    time.sleep(1)
    pt.moveTo(x,y, duration=0.5)
    pt.click()
    pt.click()
    keyboard.press_and_release('windows+up')
    time.sleep(7)

def putURL(link):
    global x, y
    x,y = 326, 50
    pt.moveTo(x,y, duration=1.5)
    pt.click()
    keyboard.write(link)
    time.sleep(2)
    keyboard.press_and_release('enter')
    time.sleep(4)

def clickLogin():
    global x, y
    x, y = 366, 459
    pt.moveTo(x,y, duration=1)
    pt.click()
    time.sleep(5)

def getRegistros():
    global x,y
    x, y = 50, 352
    pt.moveTo(x,y, duration=2.5)
    pt.doubleClick()
    time.sleep(3)
    keyboard.press_and_release('ctrl+c')
    time.sleep(1)
    registro = pyperclip.paste()
    return(registro)

def genURL(registro):
    url = "http://pgmonre.es/modulos/fraude.php?num="
    url = url + registro
    return (url) 

def cerrarChrome():
    """ os.system("taskkill /im chrome.exe /f") """
    global x,y
    x, y = 776, 12
    pt.moveTo(x,y, duration=.5)
    pt.click()

def insertBBDD(registro,urlNav):
    fecha = time.strftime('%Y-%m-%d %H:%M:%S')
    maquina = socket.gethostname()
    cnxn = pyodbc.connect(
        "Driver={SQL Server};"
        "Server=MKTCRM;"
        "Database=RPyA;"
        "Trusted_Connection=no;"
        "UID=sa;"
        "PWD=Lrnas03m01"
    )
    cursor = cnxn.cursor()
    cursor.execute('Insert into [RPyA].[dbo].[RPyA_FRAUDES] (Fecha,Registros,URLNavegada,Maquina) values(?, ?, ?, ?)', (fecha,registro,urlNav,maquina))
    cursor.commit()

def getBBDD():
    fecha = time.strftime('%Y-%m-%d %H:%M:%S')
    cnxn = pyodbc.connect(
        "Driver={SQL Server};"
        "Server=MKTCRM;"
        "Database=RPyA;"
        "Trusted_Connection=yes"
    )
    print(f"Obteniendo de la bbdd a las {fecha}")
    cursor = cnxn.cursor()
    cursor.execute('SELECT TOP (300) [id],[Registros],[URLNavegada],[Fecha]FROM [RPyA].[dbo].[RPyA_FRAUDES] ORDER BY [Fecha] DESC;')
    resultado = cursor.fetchall()   
    return resultado
    """ cursor.commit() """