from Tabela_Verdade import cls_Tabela_Verdade
from os import path

dirname = path.dirname(__file__)
print(f'Path: {dirname}')

# Input
list_cat = ['d','v','s','t']
file_name = 'tabela verdade'

# Execution
tab_verdade = cls_Tabela_Verdade(list_cat)
tab_verdade.dir_name = dirname
tab_verdade.set_file_name(file_name)
tab_verdade.create_file()
