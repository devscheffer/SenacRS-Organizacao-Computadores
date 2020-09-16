class cls_Equacao_Logica:
    def __init__(self,dir_name_in,file_name_in,file_name_out ,n_input,n_output):
        self.file_name_in = file_name_in
        self.file_name_out = file_name_out
        self.dir_name_in = dir_name_in
        self.file_path = self.get_file()
        self.data = self.create_data()
        self.list_keys = list(self.data[list(self.data.keys())[0]].keys())
        self.input = list(self.list_keys[1:n_input+1])
        self.output = list(self.list_keys[-n_output])
        self.eq_soma_produto = self.create_equation()[0]
        self.eq_produto_soma = self.create_equation()[1]

    def get_file(self):
        from os import path
        # dirname = path.dirname(__file__)
        path_file_name = f'{self.dir_name_in}\{self.file_name_in}'
        return path_file_name

    def create_data(self):
        with open(f'{self.file_path}','r') as file:
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

    def create_equation(self):
        for i in self.data.keys():
            dict_item = list(self.data[i].items())
            temp_list1 = []
            for k,v in dict_item:
                if k in self.input:
                    if int(v) == 1:
                        nom1 = f'{k}'
                    else:
                        nom1 = f'{k}\''
                    temp_list1.append(nom1)

            temp_list2 = []
            for k,v in dict_item:
                if k in self.output:
                    if v == 0:
                        nom2 = '+'.join(temp_list1)
                    else:
                        nom2 = '.'.join(temp_list1)
                    temp_list2.append(nom2)
                    self.data[i][f'eq_out_{k}'] = temp_list2[0]

        temp_list_1 = []
        temp_list_0 = []
        for i in self.data.values():
            for k,v in i.items():
                if k in self.output:
                    if int(v) == 0:
                        temp_list_0.append(i[f'eq_out_{k}'])
                    else:
                        temp_list_1.append(i[f'eq_out_{k}'])


        nom_1 = ') + ('.join(temp_list_1)
        nom_0 = ') . ('.join(temp_list_0)

        soma_produto = f'({nom_1})'
        produto_soma = f'({nom_0})'

        return soma_produto,produto_soma

    def create_file(self):
        from os import path,remove

        # dir_name = path.dirname(__file__)
        path_file_name = f'{self.dir_name_in}/{self.file_name_out}'
        if path.exists(path_file_name):
            remove(path_file_name)


        with open(f'{path_file_name}','w') as file:
            file.write(f"Soma de produto: \n {self.eq_soma_produto}")
            file.write(f"Produto de soma: \n {self.eq_produto_soma}")





