# Input
list_bit = ['d','v','s','t']

# function

def create_dict_bit(list_bit):
    dict_bit ={}
    for i in list_bit:
        key = f'{i}'
        dict_bit[key] = [0,1]
    return dict_bit

def create_combination(dict_bit):
    from itertools import product
    list_iter = []
    for i in dict_bit:
        list_iter.append(dict_bit[i])
    all_combination = list(product(*list_iter))
    return all_combination



def create_list_dict_combination(list_bit,combination):
    list_dict_combination = []
    for i in combination:
        dict_temp = {}
        for j in range(len(i)):
            dict_temp[f'{list_bit[j]}'] = i[j]
        list_dict_combination.append(dict_temp)
    return list_dict_combination


def print_elements(list_dict_combination):
    keys = list_dict_combination[0].keys()
    print(f'keys: {keys}')
    for i in keys:
        print(f'i[\'{i}\']')


def logic_output(list_dict_combination):
    '''
    Colocar as logicas de saida de acordo com as variaveis de entrada
    a saida deve ser escrita i['key_saida'] = valor_saida
    '''
    print_elements(list_dict_combination)
    for i in list_dict_combination:
        # Colocar logica aqui
        i['l'] = 1
    return list_dict_combination


def create_file(tabela_verdade,file_name = 'tabela verdade.csv'):
    from os import path,remove

    dirname = path.dirname(__file__)
    path_file_name = f'{dirname}/{file_name}'
    if path.exists(path_file_name):
        remove(path_file_name)


    with open(f'{path_file_name}','w') as file:
        keys = tabela_verdade[0].keys()
        keys_join = ','.join(keys)
        header = f'num,{keys_join}\n'
        file.write(f'{header}')
        count = 0
        for i in tabela_verdade:
            temp = map(str,list(i.values()))
            value_join = ','.join(temp)
            count += 1
            file.write(f"{count:02},{value_join}\n")

dict_bit = create_dict_bit(list_bit)
combination = create_combination(dict_bit)
list_dict_combination = create_list_dict_combination(list_bit,combination)
tabela_verdade = logic_output(list_dict_combination)
create_file(tabela_verdade)
