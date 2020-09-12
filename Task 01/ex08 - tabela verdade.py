x0 = [0,1,2,3]
x1 = [0,1,2,3]

decision = []
count = 0
for i in x0:
    for j in x1:
        count += 1
        decision.append(
            {
            'x0': i
            ,'x1': j
            }
        )

for d in decision:
    total = sum([d['x0'],d['x1']])
    d['f'] = 0
    if total > 1 or d['y'] == 1:
        d['f'] = 1


print(f'decision: {decision}')


from os import path,remove

file_name = 'tabela verdade.csv'
if path.exists(file_name):
    remove(file_name)

count = 0
with open(f'{file_name}','a+') as file:
    file.write(f'num,x0, x1, f\n')
    for i in decision:
        count += 1
        file.write(f"{count:02},{i['x0']},{i['x1']},{i['f']}\n")
