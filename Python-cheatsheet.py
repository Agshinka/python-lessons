# STRINGS
print(f'Apple has {len('apple')} letters.')  ## Считаем кол-во букв. !Output 5!

print('APPLE'.lower())  ## Делаем все маленьким !Output apple!

print('apple'.upper())  ## Ну а тут все большое !Output APPLE!


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

