from Tools.tabela_verdade import cls_Tabela_Verdade
from Tools.equacao_logica import cls_Equacao_Logica
from os import path

# Input
dirname = path.dirname(__file__)
print(f"Path: {dirname}")
file_name_out = "tab_verdade T1.csv"
list_cat_in = ["a", "b", "c"]


# Criacao tabela verdade
tab_verdade = cls_Tabela_Verdade(
    dirname
    , list_cat_in
    , file_name_out
    )
tab_verdade.create_file()



# def create_logic_output(self):
#     '''
#     Colocar as logicas de saida de acordo com as variaveis de entrada
#     a saida deve ser escrita i['key_saida'] = valor_saida
#     '''
#     keys = self.list_dict_combination[0].keys()
#     print(f'{"="*20}')
#     print(f'keys: {keys}')
#     for i in keys:
#         print(f'i[\'{i}\']')
#     print(f'{"="*20}')

#     print(self.list_dict_combination)
#     for i in self.list_dict_combination:
#         total = sum(i.values())
#         vote_d = i['d']
#         if (total == 2 and  vote_d == 1) or (total > 2):
#             i['L'] = 1
#         else:
#             i['L'] = 0
#     return self.list_dict_combination
# # Criacao equacao logica
# file_name_eq_logica = "Equacao Logica.csv"
# n_output = 1
# file = cls_Equacao_Logica(
#     dirname
#     , file_name_out
#     , file_name_eq_logica
#     , len(list_cat_in)
#     , n_output
#     )
# file.create_file()
