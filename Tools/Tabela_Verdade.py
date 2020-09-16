class cls_Tabela_Verdade:
    def __init__(self,list_cat):
        print(f'Objeto em andamento')
        self.list_cat = list_cat
        self.file_name = 'tabela verdade.csv'
        self.dir_name = ''
        print(f'Objeto criado 1: {self.list_cat}')
        self.dict_cat = self.create_dict_cat()
        print(f'Objeto criado 2: {self.dict_cat}')
        self.all_combination = self.create_combination()
        print(f'Objeto criado 3: {self.all_combination}')
        self.list_dict_combination = self.create_list_dict_combination()
        print(f'Objeto criado 4: {self.list_dict_combination}')
        self.logic_output = self.create_logic_output()
        print(f'Objeto criado 5: {self.logic_output}')


    def create_dict_cat(self):
        dict_cat ={}
        for i in self.list_cat:
            key = f'{i}'
            dict_cat[key] = [0,1]
        return dict_cat

    def create_combination(self):
        from itertools import product
        list_iter = []
        for i in self.dict_cat:
            list_iter.append(self.dict_cat[i])
        all_combination = list(product(*list_iter))
        return all_combination



    def create_list_dict_combination(self):
        list_dict_combination = []
        for i in self.all_combination:
            dict_temp = {}
            for j in range(len(i)):
                dict_temp[f'{self.list_cat[j]}'] = i[j]
            list_dict_combination.append(dict_temp)
        return list_dict_combination


    def create_logic_output(self):
        '''
        Colocar as logicas de saida de acordo com as variaveis de entrada
        a saida deve ser escrita i['key_saida'] = valor_saida
        '''
        keys = self.list_dict_combination[0].keys()
        print(f'{"="*20}')
        print(f'keys: {keys}')
        for i in keys:
            print(f'i[\'{i}\']')
        print(f'{"="*20}')

        print(self.list_dict_combination)
        for i in self.list_dict_combination:
            total = sum(i.values())
            vote_d = i['d']
            if (total == 2 and  vote_d == 1) or (total > 2):
                i['L'] = 1
            else:
                i['L'] = 0
        return self.list_dict_combination


    def create_file(self):
        from os import path,remove

        # dirname = path.dirname(__file__)
        path_file_name = f'{self.dir_name}/{self.file_name}'
        if path.exists(path_file_name):
            remove(path_file_name)


        with open(f'{path_file_name}','w') as file:
            keys = self.logic_output[0].keys()
            keys_join = ','.join(keys)
            header = f'num,{keys_join}\n'
            file.write(f'{header}')
            count = 0
            for i in self.logic_output:
                temp = map(str,list(i.values()))
                value_join = ','.join(temp)
                count += 1
                file.write(f"{count:02},{value_join}\n")

    def set_file_name(self,name):
        self.file_name = f'{name}.csv'


