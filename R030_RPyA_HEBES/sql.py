import pyodbc
import time
import ctypes  # An included library with Python install.
import mysql.connector
import mysql.connector
from mysql.connector import Error


def InsertBBDD(InsertQuery):
    cnxn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=172.17.11.7;"
    "Database=ZEUS;"
    "Trusted_Connection=yes")

    fecha = time.strftime('%Y-%m-%d %H:%M:%S')
    print(f"Insertando en la bbdd a las {fecha} query {InsertQuery}")
    
    cursor = cnxn.cursor()
    cursor.execute(InsertQuery)
    cnxn.commit()

def UpdateBBDD():
    cnxn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=MKTCRM;"
    "Database=RPyA;"
    "Trusted_Connection=yes")
    UpdateQuery = "truncate table [RPyA].[dbo].[RPyA_MM_HEBES]"
    fecha = time.strftime('%Y-%m-%d %H:%M:%S')
    print(f"Updating BBDD en la bbdd a las {fecha}")
    cursor = cnxn.cursor()
    cursor.execute(UpdateQuery)
    cnxn.commit()

def execBBDD():
    cnxn = mysql.connector.connect(host='172.17.11.7',
                                         database='ZEUS',
                                         user='root',
                                         password='Lrnas03m01')

    ExecQuery = f"call AsignarAgentesHemes"
    fecha = time.strftime('%Y-%m-%d %H:%M:%S')
    cursor = cnxn.cursor()
    cursor.execute(ExecQuery)
    cnxn.commit()
    print(f"Agentes carterizados BBDD en la bbdd a las {fecha}")

def GetBBDD(resultado):
    fecha = time.strftime('%Y-%m-%d %H:%M:%S')
    cnxn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=MKTCRM;"
    "Database=RPyA;"
    "Trusted_Connection=yes")
    print(f"Obteniendo Carteización la bbdd a las {fecha}")
    cursor = cnxn.cursor()
    cursor.execute('SELECT TOP (1000) [RazonSocial],[NumeroDocumento],[IdCliente],[Idservicio],[FechaVenta],[FechaCita],[FechaInstalación],[FechaPreactivación],[FechActivación],[FechaCancelación],[MotivoCancelación],[FechaBaja],[MotivoBaja],[OTInicial],[FechaOTInicial],[OTActual],[NombreOTActual],[EstadoOTActual],[FechaOTActual],[FechaCierreOT],[FechaPrevistaPortabilidadVC],[FechaPortabilidad],[EstadoPortabilidad],[OperadorPortabilidad],[SegmentoCanal],[CanalMaestro],[Supercanal],[Subcanal],[Vendedor],[Tiposervicio],[Tecnologia],[Terminal],[TipoMovilInicial],[TipoMovilActual],[Descuentos],[Campaña],[Origen],[TipoContrato],[TipoFactura],[Enlinea],[TipoPaquete],[ICCID],[NuevaVenta],[TipoVenta],[MotivoCancelacionProv],[MotivoJira],[SubmotivoJira],[RPAdo],[Email],[Agente] FROM [RPyA].[dbo].[RPyA_MM_HEBES]')
    resultado = cursor.fetchall()
    ctypes.windll.user32.MessageBoxW(0, str(resultado), "Clientes Insertados", 1)


    cursor.execute('SELECT TOP (1000) [RazonSocial],[IdCliente],[Idservicio],[Agente] FROM [RPyA].[dbo].[RPyA_MM_HEBES]')
    resultado = cursor.fetchall()
    """ ctypes.windll.user32.MessageBoxW(0, str(resultado), "Clientes Carterizados", 1) """   
    return resultado

def InsertZeus(InsertQuery):
    try:
        connection = mysql.connector.connect(host='172.17.11.7',
                                         database='ZEUS',
                                         user='root',
                                         password='Lrnas03m01')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute(InsertQuery)
            connection.commit()
            """ cursor.execute("select * from RPyA_MM_HEBES;")
            record = cursor.fetchone()
            print("You're connected to database: ", record) """

    except Error as e:
            print("Error while connecting to MySQL", e)
    finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")

def TuncateZeus():

    try:
        connection = mysql.connector.connect(host='172.17.11.7',
                                         database='ZEUS',
                                         user='root',
                                         password='Lrnas03m01')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            TruncateQuery = "truncate table RPyA_MM_HEBES;"
            cursor.execute(TruncateQuery)
            connection.commit()
            """ cursor.execute("select * from RPyA_MM_HEBES;")
            record = cursor.fetchone()
            print("You're connected to database: ", record) """

    except Error as e:
            print("Error while connecting to MySQL", e)
    finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed after truncating")

def CarterizarDatosInsertados(agentes):
    try:
        connection = mysql.connector.connect(host='172.17.11.7',
                                         database='ZEUS',
                                         user='root',
                                         password='Lrnas03m01')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            ExecQuery = f"exec [AsignarAgentesHemes] {str(agentes)}"
            fecha = time.strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute('SELECT TOP (1000) [RazonSocial],[NumeroDocumento],[IdCliente],[Idservicio],[FechaVenta],[FechaCita],[FechaInstalación],[FechaPreactivación],[FechActivación],[FechaCancelación],[MotivoCancelación],[FechaBaja],[MotivoBaja],[OTInicial],[FechaOTInicial],[OTActual],[NombreOTActual],[EstadoOTActual],[FechaOTActual],[FechaCierreOT],[FechaPrevistaPortabilidadVC],[FechaPortabilidad],[EstadoPortabilidad],[OperadorPortabilidad],[SegmentoCanal],[CanalMaestro],[Supercanal],[Subcanal],[Vendedor],[Tiposervicio],[Tecnologia],[Terminal],[TipoMovilInicial],[TipoMovilActual],[Descuentos],[Campaña],[Origen],[TipoContrato],[TipoFactura],[Enlinea],[TipoPaquete],[ICCID],[NuevaVenta],[TipoVenta],[MotivoCancelacionProv],[MotivoJira],[SubmotivoJira],[RPAdo],[Email],[Agente] FROM [RPyA].[dbo].[RPyA_MM_HEBES]')
            resultado = cursor.fetchall()
            ctypes.windll.user32.MessageBoxW(0, str(resultado), "Clientes Insertados", 1)

    except Error as e:
            print("Error while connecting to MySQL", e)
    finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")

def GetZeus(resultado):

    try:
        connection = mysql.connector.connect(host='172.17.11.7',
                                         database='ZEUS',
                                         user='root',
                                         password='Lrnas03m01')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            ExecQuery = f"exec [AsignarAgentesHemes]"
            fecha = time.strftime('%Y-%m-%d %H:%M:%S')
            cursor.execute(ExecQuery)
            connection.commit()
            print(f"Agentes carterizados BBDD en la bbdd a las {fecha}")
            """ cursor.execute("select * from RPyA_MM_HEBES;")
            record = cursor.fetchone()
            print("You're connected to database: ", record) """

    except Error as e:
            print("Error while connecting to MySQL", e)
    finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")

    """ fecha = time.strftime('%Y-%m-%d %H:%M:%S')
    cnxn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=MKTCRM;"
    "Database=RPyA;"
    "Trusted_Connection=yes")
    print(f"Obteniendo Carteización la bbdd a las {fecha}")
    cursor = cnxn.cursor()
    cursor.execute('SELECT TOP (1000) [RazonSocial],[NumeroDocumento],[IdCliente],[Idservicio],[FechaVenta],[FechaCita],[FechaInstalación],[FechaPreactivación],[FechActivación],[FechaCancelación],[MotivoCancelación],[FechaBaja],[MotivoBaja],[OTInicial],[FechaOTInicial],[OTActual],[NombreOTActual],[EstadoOTActual],[FechaOTActual],[FechaCierreOT],[FechaPrevistaPortabilidadVC],[FechaPortabilidad],[EstadoPortabilidad],[OperadorPortabilidad],[SegmentoCanal],[CanalMaestro],[Supercanal],[Subcanal],[Vendedor],[Tiposervicio],[Tecnologia],[Terminal],[TipoMovilInicial],[TipoMovilActual],[Descuentos],[Campaña],[Origen],[TipoContrato],[TipoFactura],[Enlinea],[TipoPaquete],[ICCID],[NuevaVenta],[TipoVenta],[MotivoCancelacionProv],[MotivoJira],[SubmotivoJira],[RPAdo],[Email],[Agente] FROM [RPyA].[dbo].[RPyA_MM_HEBES]')
    resultado = cursor.fetchall()
    ctypes.windll.user32.MessageBoxW(0, str(resultado), "Clientes Insertados", 1)


    cursor.execute('SELECT TOP (1000) [RazonSocial],[IdCliente],[Idservicio],[Agente] FROM [RPyA].[dbo].[RPyA_MM_HEBES]')
    resultado = cursor.fetchall()
    ctypes.windll.user32.MessageBoxW(0, str(resultado), "Clientes Carterizados", 1)   
    return resultado """

def DisplayCarterizacion():
    resultado = ()
    resultadoQuery = GetBBDD(resultado)

    for c,registro in enumerate(resultadoQuery):
        try:
            carterizacion = f"Razon Social: {resultadoQuery[c][0]} - IDCliente: {resultadoQuery[c+1][1]} - Número de Agente Asignado: {resultadoQuery[c+3][3]}"
        except:
            continue
        strcarterizacion = ''.join(carterizacion)
        ctypes.windll.user32.MessageBoxW(0, str(strcarterizacion), "Clientes Carterizados", 1)
        print(strcarterizacion)