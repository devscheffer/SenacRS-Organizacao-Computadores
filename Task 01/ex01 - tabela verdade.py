A = [0,1]
B = [0,1]
C = [0,1]

decision = []
count = 0
for i in A:
    for j in B:
        for k in C:
            count += 1
            decision.append(
                {
                'A': i
                ,'B': j
                ,'C': k
                }
            )

for d in decision:
    total = sum([d['A'],d['B'],d['C']])
    d['D'] = d['E'] = d['F'] = 0
    if total > 0:
        d['D'] = 1
    if total == 2:
        d['E'] = 1
    if total == 3:
        d['F'] = 1
print(f'decision: {decision}')


from os import path,remove

file_name = 'tabela verdade.csv'
if path.exists(file_name):
    remove(file_name)

count = 0
with open(f'{file_name}','a+') as file:
    file.write(f'num,A, B, C, D, E, F\n')
    for i in decision:
        count += 1
        file.write(f"{count:02},{i['A']},{i['B']},{i['C']},{i['D']},{i['E']},{i['F']}\n")
