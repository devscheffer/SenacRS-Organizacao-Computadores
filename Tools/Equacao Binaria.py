
def create_data(path_file_name):
    with open(f'{path_file_name}','r') as file:
        a = file.read().splitlines()
        keys = a[0].split(sep=',')
        data = {}

        for i in a[1:]:
            i = i.split(sep=',')
            temp_dict = {}
            for j in range(len(i)):
                temp_dict[f'{keys[j]}'] = i[j]
            key_temp = temp_dict[f'{keys[0]}']
            data[f'{key_temp}'] = temp_dict
        return data

def get_file(file_name = 'tabela verdade.csv'):
    from os import path

    dirname = path.dirname(__file__)
    path_file_name = f'{dirname}/{file_name}'
    return path_file_name

file = get_file()
data = create_data(file)


list_keys = list(data[list(data.keys())[0]].keys())
n_input = 4
n_output = 1
input = list_keys[1:n_input+1]
output = list_keys[-n_output]

for i in data.keys():
    dict_item = list(data[i].items())
    temp_list1 = []
    for k,v in dict_item:
        if k in input:
            if int(v) == 1:
                nom1 = f'{k}'
            else:
                nom1 = f'{k}\''
            temp_list1.append(nom1)

    temp_list2 = []
    for k,v in dict_item:
        if k in output:
            if v == 0:
                nom2 = '+'.join(temp_list1)
            else:
                nom2 = '.'.join(temp_list1)
            temp_list2.append(nom2)
            data[i][f'eq_out_{k}'] = temp_list2[0]

temp_list_1 = []
temp_list_0 = []
for i in data.values():
    for k,v in i.items():
        if k in output:
            if int(v) == 0:
                temp_list_0.append(i[f'eq_out_{k}'])
            else:
                temp_list_1.append(i[f'eq_out_{k}'])


nom_1 = ') + ('.join(temp_list_1)
nom_0 = ') . ('.join(temp_list_0)

soma_produto = f'Soma de produto:\n({nom_1})'
produto_soma = f'Produto de soma:\n({nom_0})'

print(soma_produto)
print(produto_soma)
