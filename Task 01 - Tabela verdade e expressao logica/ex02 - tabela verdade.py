g = [0,1]
a = [0,1]
t = [0,1]

decision = []
count = 0
for i in g:
    for j in a:
        for k in t:
            count += 1
            decision.append(
                {
                'g': i
                ,'a': j
                ,'t': k
                }
            )

for d in decision:
    total = sum([d['g'],d['a'],d['t']])
    d['c'] = 0
    if d['t'] == 1 and total > 1:
        d['c'] = 1

print(f'decision: {decision}')


from os import path,remove

file_name = 'tabela verdade.csv'
if path.exists(file_name):
    remove(file_name)

count = 0
with open(f'{file_name}','a+') as file:
    file.write(f'num,g, a, t, c\n')
    for i in decision:
        count += 1
        file.write(f"{count:02},{i['g']},{i['a']},{i['t']},{i['c']}\n")
