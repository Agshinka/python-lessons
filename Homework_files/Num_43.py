import random

a=''
b=random.randint(1,100)
while a != b:
    a=int(input('Введите число:\n'))
    if a < 1 or a > 100:
        print('Ваше число не соотвествует интервалу!\n')
        continue
    if a > b:
        print('Ваш ответ больше!')
    elif a < b:
        print('Ваш ответ меньше!')
print(f'Вы угадали! Было загадано число: {b}')