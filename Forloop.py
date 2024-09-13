print(type(range))
numbers=list(range (1,10))
print(numbers)

even_numbers=list(range (2,11,2))
print(even_numbers)

for n in range (2,10):
    print('*'*10)
    for k in range (2,10):
        print(f'{n}*{k}={n*k}')

