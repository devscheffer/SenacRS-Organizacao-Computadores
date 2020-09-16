from Tools.tabela_verdade import cls_Tabela_Verdade
from Tools.equacao_logica import cls_Equacao_Logica
from os import path

dirname = path.dirname(__file__)
print(f"Path: {dirname}")

# Input
list_cat = ["d", "v", "s", "t"]
file_name_tabela_verdade = "tabela verdade.csv"
file_name_eq_logica = "Equacao Logica.csv"
n_output = 1

# Criacao tabela verdade
tab_verdade = cls_Tabela_Verdade(
    dirname
    , list_cat
    , file_name_tabela_verdade
    )
tab_verdade.create_file()

# Criacao equacao logica
file = cls_Equacao_Logica(
    dirname
    , file_name_tabela_verdade
    , file_name_eq_logica
    , len(list_cat)
    , n_output
    )
file.create_file()
