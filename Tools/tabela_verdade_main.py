from tabela_verdade_cls import cls_Tabela_Verdade
from os import path

# Input
dirname = path.dirname(__file__)
TV_file_name_out = "tab_verdade T1.csv"
list_cat_in = ["A", "B", "C"]


# Criacao tabela verdade
tab_verdade = cls_Tabela_Verdade (
    dirname
    , list_cat_in
    , TV_file_name_out
    )

# Lógica das variaveis de saida
list_dict_tab_verdade = tab_verdade.list_dict_combination

for i in list_dict_tab_verdade:
    i['D'] = i['E'] = i['F'] = 0
    total = sum([i['A'],i['B'],i['C']])
    if total > 0:
        i['D'] = 1
    if total == 2:
        i['E'] = 1
    if total == 3:
        i['F'] = 1

tab_verdade.create_file(list_dict_tab_verdade)

