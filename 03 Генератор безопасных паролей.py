import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
nogood = 'il1Lo0O'

chars = ''

number = input('\nСколько паролей вам нужно сгенерировать? ' )
length = input('\nУкажите желаемую длину пароля? ')

print('\nЧТО БУДЕТ В ВАШЕМ ПАРОЛЕ?')
digit = input(f'\nВключить цифры {digits} в пароль? (y = да, n = нет) ')
up_letters = input(f'\nВключить ПРОПИСНЫЕ буквы {uppercase_letters} в пароль? (y = да, n = нет) ')
low_letters = input(f'\nВключить строчные буквы {lowercase_letters} в пароль? (y = да, n = нет) ')
symbols = input(f'\nВключить символы {punctuation} в пароль? (y = да, n = нет) ')
exclude = input(f'\nИсключить неоднозначные символы {nogood} из пароля? (y = да, n = нет) ')

if digit.lower() == 'y':
    chars += digits
if up_letters.lower() == 'y':
    chars += uppercase_letters        
if low_letters.lower() == 'y':
    chars += lowercase_letters
if symbols.lower() == 'y':
    chars += punctuation
if exclude == 'y':
    for i in nogood:
        if i in chars:
            chars = chars.replace(i, '')
print('\nВот симовлы, из которых будет пароль' , chars)
    
def generate_password(length, chars):
    return random.sample(chars, int(length))

for _ in range(int(number)):
    print(* generate_password(int(length), chars), sep='')
    