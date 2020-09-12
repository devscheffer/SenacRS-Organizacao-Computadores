a = [0,1]
b = [0,1]
c = [0,1]

decision = []
count = 0
for i in a:
    for j in b:
        for k in c:
            count += 1
            decision.append(
                {
                'a': i
                ,'b': j
                ,'c': k
                }
            )

for d in decision:
    total = sum([d['a'],d['b'],d['c']])
    d['f2'] = 0
    if (d['a'] + d['b'] > 0) and d['c'] == 1:
        d['f2'] = 1

print(f'decision: {decision}')


from os import path,remove

file_name = 'tabela verdade.csv'
if path.exists(file_name):
    remove(file_name)

count = 0
with open(f'{file_name}','a+') as file:
    file.write(f'num,a, b, c, f2\n')
    for i in decision:
        count += 1
        file.write(f"{count:02},{i['a']},{i['b']},{i['c']},{i['f2']}\n")
