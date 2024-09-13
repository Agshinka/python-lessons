import math
from math import sqrt, floor
# STRINGS
print(f'Apple has {len('apple')} letters.')  ## Считаем кол-во букв. !Output 5!

print('APPLE'.lower())  ## Делаем все маленьким !Output apple!

print('apple'.upper())  ## Ну а тут все большое !Output APPLE!

print('apple'.count('p')) # Считает конкретно то, что хотим (2)

print('Hello world.'.replace('.','!').replace('l','h',1))


# SPLIT
print('apple, chery, orange'.split(','))

print('-'.join(['chocolate', 'milk', 'cheese']))


# SLICING
text='Hello there!'
print(text[0])       ## С конкретного индекса
print(text[-1])

print(text[0:3])     ## Так же 
print(text[:3])

print(text[3:])  

print(text[::])  ## Копировать текст

print(text[0:5:2])  ## Через букву вывод

print(text[::-1])  ## Копировать в обратном порядке


# Math
print(sum([45, 76]))  #Принимает лист и складывает значения

print(max(34, 67))  #Ищет максимум из двух чисел

print(min(34, 67))  #Противоположно работает

print((bin(5)))    #Эта функция переводит любое десятичное число в двоичную сс, возвращает текст и требует обрезания первых двух символов

print(int(3.7))

print(float('5'))

print(f'Корень квадратный из четырех {sqrt(4)}') #Корень 4 (2.0)

print(f'{floor(2.6)}')  #Округление любого числа в меньшую сторону (2)

print(f'{math.ceil(2.7)}') #Округляет любое число в большую сторону (3)

print(f'{round(2.5)}') #Сам решает, как округлить (2)

print(f'{round(2.555,2)}')

print(pow(2,5))

print(7%2)

print('Четное' if 7%2==0 else 'Нечетное')