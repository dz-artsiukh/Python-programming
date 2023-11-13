import random

right = 100
num = random.randint(1, right)

print('Добро пожаловать в числовую угадайку')

c = 0
again = 'y'

def is_valid(num):
    return num.isdigit() and 1 <= int(num) <= 100


while again.lower() == 'y':
    n = input(f'Введите число от 1 до {right} ')
    if is_valid(n) == False:
        print(f'А может быть все-таки введем целое число от 1 до {right}?')
    else:
        n = int(n)
        c += 1
        if n < num:
            print('\nВаше число МЕНЬШЕ загаданного, попробуйте еще разок')
        elif n > num:
            print('\nВаше число БОЛЬШЕ загаданного, попробуйте еще разок')
        elif n == num:
            print('\nВы УГАДАЛИ, поздравляем!')
            print(f'Числов ваших попыток составило {c}')
            again = input(f'Хотите сыграть еще раз? (y = да n = нет)')
            if again == 'y':
                right = int(input('\n Выберите правую границу чисел '))
                num = random.randint(1, right)
            else:
                print('Спасибо, что играли в числовую угадайку. Еще увидимся...')

n = input()
print(is_valid(n))