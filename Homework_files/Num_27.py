a=float(input('Введите заработок:\n'))
if a<1000:
    print(f'Вам начислен бонус 100! {a+100}')
elif a>1000 and a<2000:
    print(f'Ваша сумма удвоилась! {a*2}')
elif a>2000:
    print(f'К сожалению, ваша сумма осталась неизменна. {a}')

# f1=int(input())
# f2=int(input())
# f3=int(input())
# print(f'Total = {f1+f2+f3}')