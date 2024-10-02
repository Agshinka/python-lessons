# import pdb
# pdb.set_trace()

total=0
for n in range (7):
    a=int(input(f'Введите температуру {n+1}\n'))
    total+=a
total=total/7
print(total)