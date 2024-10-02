a=[0]
b=[input('What is your name?\n')]
for n in range (len(a)):
    for x in range(len(b)):
        a[n]=int(input('How old are you?\n'))
        if a[n] <= 12:
            print (f'{b[x]} - Junior')
        elif 12 <= a[n] <= 17:
            print (f'{b[x]} - Teenager')
        else:
            print (f'{b[x]} - Adult')
