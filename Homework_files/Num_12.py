a=int(input('Стоимость первого лота:\n'))
b=int(input('Стоимость второго лота:\n'))
c=int(input('Стоимость третьего лота:\n'))

d=((a+b+c)/100)*10
e=(a+b+c)-d

print(round(e))