from typing import NoReturn
from openpyxl import load_workbook
from time import sleep
import sql

def insertarExcel(excelpath):
    book = load_workbook(excelpath)
    sheet = book.active
    rows = sheet.rows
    headers = [cell.value for cell in next((rows))]
    all_rows = []
    sql.truncateBBDD()
    print("borrao")
    sleep(5)
    for i,row in enumerate(rows):
        if i >= 6:
            a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p = row
            fecha = a.value
            intervalo = b.value
            cola = c.value
            tipomedio = d.value
            ofrecidas = e.value
            contestadas = f.value
            abandonadas = g.value
            porcentajeabandonadas = h.value
            porcentajeSLA = i.value
            ASA = j.value
            Convmedia = k.value
            ACWmedio = l.value
            AHT = m.value
            retencionmedia = n.value
            transferidas = o.value
            porcentajetransferencia = p.value
            
            sqlQuery = "Insert into [RPyA].[dbo].[RPyA_2MARES] (RPAdo,Fecha,Intervalo,Cola,TipoMedio,Ofrecidas,contestadas,Abandonadas,PorcentajeAbandonadas,PorcentajeSLA,ASA,ConvMedia,ACWmedio,AHT,Retenciónmedia,Transferidas,PorcentajeTransferencia) values ('01','"+str(fecha)+"','"+str(intervalo)+"','"+str(cola)+"','"+str(tipomedio)+"','"+str(ofrecidas)+"','"+str(contestadas)+"','"+str(abandonadas)+"','"+str(porcentajeabandonadas)+"', '"+str(porcentajeSLA)+"', '"+str(ASA)+"', '"+str(Convmedia)+"', '"+str(ACWmedio)+"', '"+str(AHT)+"', '"+str(retencionmedia)+"', '"+str(transferidas)+"', '"+str(porcentajetransferencia)+"')"
            
            print(sqlQuery)
            sql.InsertBBDD(sqlQuery)