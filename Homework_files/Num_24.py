a=input('Введите текст:\n')
c=input('Введите текст 2:\n')
b=a.count('a')+a.count('e')+a.count('o')+a.count('u')+a.count('i')
d=c.count('a')+c.count('e')+c.count('o')+c.count('u')+c.count('i')
perc1=(len(a)*b)/100
perc2=(len(c)*d)/100
if perc1 > perc2:
    print('Предложение 1 больше')
elif perc2 > perc1:
    print('Предложение 2 больше')