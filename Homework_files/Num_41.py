limit = 200
a = 0
presents = 0
while presents <= limit:
    a=float(input('Введите стоимость:\n'))
    presents += a
print(f'Лимит превышен!\n {a}')