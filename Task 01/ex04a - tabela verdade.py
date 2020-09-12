x = [0,1]
y = [0,1]

decision = []
count = 0
for i in x:
    for j in y:
        count += 1
        decision.append(
            {
            'x': i
            ,'y': j
            }
        )

for d in decision:
    total = sum([d['x'],d['y']])
    d['f1'] = 0
    if total > 1 or d['y'] == 1:
        d['f1'] = 1


print(f'decision: {decision}')


from os import path,remove

file_name = 'tabela verdade.csv'
if path.exists(file_name):
    remove(file_name)

count = 0
with open(f'{file_name}','a+') as file:
    file.write(f'num,x, y, f1\n')
    for i in decision:
        count += 1
        file.write(f"{count:02},{i['x']},{i['y']},{i['f1']}\n")
