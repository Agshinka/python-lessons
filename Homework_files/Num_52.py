lis=['Melissa', 'Evelyn', 'Emmy', 'Karen', 'Norma', 'Dorek', 'Agnes', 'Billy', 'Gawel', 'Arthur']
answer=[]
for n in range (len(lis)):
    a=input(f'{lis[n]} Вы придете на день рождение?\n')
    if a == 'No':
        answer.append(False)
    elif a == 'Yes':
        answer.append(True)

for x in range (len(answer)):
    if answer[x]:
        print(lis[x])