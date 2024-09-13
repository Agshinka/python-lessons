user_input=''
a=0
while a<=10:
    a+=1
    print(a)

while len (user_input) < 2:
    user_input=input('Введите имя:\n')

print(user_input)


char = 'p'
while char not in 'asdf':
    char=input('Введите другую букву:\n')
    print(char)