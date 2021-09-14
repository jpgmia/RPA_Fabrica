import RPA
urlMM = r"https://masmovil.lightning.force.com/lightning/r/Report/00O4I000004fs8BUAQ/view?queryScope=userFolders"

RPA.cleanUp()
RPA.abrirChrome()
RPA.putURL(urlMM)
RPA.clickLogin()
registro = RPA.getRegistros()
urlNav = RPA.genURL(registro)
RPA.putURL(urlNav)
RPA.cerrarChrome()
RPA.insertBBDD(registro,urlNav)