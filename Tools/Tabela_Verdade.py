class cls_Tabela_Verdade:
    def __init__(self,dir_name,list_cat,file_name):
        self.dir_name = dir_name
        self.file_name = file_name
        self.list_cat = list_cat
        self.dict_cat = self.create_dict_cat()
        self.all_combination = self.create_combination()
        self.list_dict_combination = self.create_list_dict_combination()


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

    def create_file(self):
        from os import path,remove

        path_file_name = f'{self.dir_name}/{self.file_name}'
        if path.exists(path_file_name):
            remove(path_file_name)

        with open(f'{path_file_name}','w') as file:
            keys = self.list_dict_combination[0].keys()
            keys_join = ','.join(keys)
            header = f'num,{keys_join}\n'
            file.write(f'{header}')
            count = 0
            for i in self.list_dict_combination:
                temp = map(str,list(i.values()))
                value_join = ','.join(temp)
                count += 1
                file.write(f"{count:02},{value_join}\n")



