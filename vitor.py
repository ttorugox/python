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
excel.sheets['Plan1']['A1'].value = 'CONTROLE FINANCEIRO'
excel.sheets['Plan1']['A3'].value = 'Água'
excel.sheets['Plan1']['A4'].value = 'Luz'
excel.sheets['Plan1']['A5'].value = 'Telefone'
excel.sheets['Plan1']['A6'].value = 'Supermercado'
excel.sheets['Plan1']['A8'].value = 'TOTAL'


excel.sheets['Plan1']['C2'].value = 'Janeiro'
excel.sheets['Plan1']['C3'].value = '80,00'
excel.sheets['Plan1']['C4'].value = '180,00'
excel.sheets['Plan1']['C5'].value = '200,00'
excel.sheets['Plan1']['C6'].value = '700,00'
excel.sheets['Plan1']['C8'].value = '1.160,00'

excel.sheets['Plan1']['D2'].value = 'Fevereiro'
excel.sheets['Plan1']['D3'].value = '90,00'
excel.sheets['Plan1']['D4'].value = '190,00'
excel.sheets['Plan1']['D5'].value = '210,00'
excel.sheets['Plan1']['D6'].value = '710,00'
excel.sheets['Plan1']['D8'].value = '1.200,00'


excel.sheets['Plan1']['E2'].value = 'Março'
excel.sheets['Plan1']['E3'].value = '100,00'
excel.sheets['Plan1']['E4'].value = '200,00'
excel.sheets['Plan1']['E5'].value = '220,00'
excel.sheets['Plan1']['E6'].value = '820,00'
excel.sheets['Plan1']['E8'].value = '1.340,00'