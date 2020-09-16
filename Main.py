from Tools.tabela_verdade import cls_Tabela_Verdade
from Tools.equacao_logica import cls_Equacao_Logica
from os import path

dirname = path.dirname(__file__)
print(f'Path: {dirname}')

# Input
list_cat = ['d','v','s','t']
file_name = 'tabela verdade'

# Criacao tabela verdade
tab_verdade = cls_Tabela_Verdade(list_cat)
tab_verdade.dir_name = dirname
tab_verdade.set_file_name(file_name)
tab_verdade.create_file()

# Criacao equacao logica
file = cls_Equacao_Logica(dirname,'tabela verdade.csv','Equacao Logica.csv',4,1)
file.create_file()
