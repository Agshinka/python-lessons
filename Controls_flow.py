a=int(input())
if a>1 or True:
    print('а больше одного')


if a<1 or False:
    print('a меньше одного')
else:
    print('Мое если не правда')


if a==1 or True:
    print('Ровно один!')
elif a!=1 or True:
    print('Упс, теперь нет')


is_adult=True if a>=18 else False
print(is_adult)


if is_adult:
    print('Пора найти работу!')
else:
    print('Попроси денег у мамы!')