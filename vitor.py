    #Importar biblioteca 'xlwings = modificar planilha' e 'os = mapear arquivos'
import xlwings as xl
import os

    #Mapeamento do diretório e arquivo
pasta = os.path.dirname(__file__)
arquivo = os.path.basename(__file__)[:-3]
arqExcel = pasta + "\\" + arquivo + ".xlsm"

#Alterações do arquivo excel
#Trazer arquivo para uma variável local
excel = xl.Book(arqExcel)

#Editar conteúdo da planilha
excel.sheets['Plan1']['C3'].value = 'teste'