'''
    Nombre: 2MARES
    Author: Juan Pablo Garica
    Fecha creación: 16/08/2021
    Fecha Ult. modificación: 23/01/2021
'''
import RPA
import glob
import excel2sql
RPA.cleanUp()
RPA.importarCorteSelenium()

## Exportar Selenium
path = r"C:\Users\jpgarcia\Downloads\\" 
downloads = glob.glob(path+"*Corte Automatizado*.xlsx")
for download in downloads:
    print('Exportar a Excel --->')
    print(download)
    print('Borrar a Excel ---> y Generar Funnel')
    excel2sql.insertarExcel(download)
## Generar Fichero
RPA.generarFichero() 
    