d = [0,1]
v = [0,1]
s = [0,1]
t = [0,1]

decision = []

for i in d:
    for j in v:
        for k in s:
            for l in t:
                decision.append(
                    {
                    'D': i
                    ,'V': j
                    ,'S': k
                    ,'T': l
                    }
                )

for i in decision:
    total = sum(i.values())
    vote_d = i['D']
    if (total == 2 and  vote_d == 1) or (total > 2):
        result = f'{i} - L = 1'
        i['L'] = 1
    else:
        result = f'{i} - L = 0'
        i['L'] = 0
    print(result)

from os import path,remove

file_name = 'tabela verdade.csv'
if path.exists(file_name):
    remove(file_name)

count = 0
with open(f'{file_name}','a+') as file:
    file.write(f'num,D, V, T, S, L\n')
    for i in decision:
        count += 1
        file.write(f"{count:02},{i['D']},{i['V']},{i['T']},{i['S']},{i['L']}\n")
