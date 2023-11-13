ru_alpha_0 = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
ru_alpha_1 = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
en_alpha_0 = 'abcdefghijklmnopqrstuvwxyz'
en_alpha_1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
again = 'y'

def encr_RU(text, step):
    enc_text = ''
    for i in text:
        if i in ru_alpha_0:
            enc_text += ru_alpha_0[(ru_alpha_0.index(i) + step) % 31]
        elif i in ru_alpha_1:
            enc_text += ru_alpha_1[(ru_alpha_1.index(i) + step) % 31]
        else:
            enc_text += i
    return enc_text



def decr_RU(text, step):
    decr_text = ''
    for i in text:
        if i in ru_alpha_0:
            decr_text += ru_alpha_0[abs((ru_alpha_0.index(i) - step) % 32)]
        elif i in ru_alpha_1:
            decr_text += ru_alpha_1[abs((ru_alpha_1.index(i) - step) % 32)]
        else:
            decr_text += i
    return decr_text
    
def encr_EN(text, step):
    enc_text = ''
    for i in text:
        if i in en_alpha_0:
            enc_text += en_alpha_0[(en_alpha_0.index(i) + step) % 26]
        elif i in en_alpha_1:
            enc_text += en_alpha_1[(en_alpha_1.index(i) + step) % 26]
        else:
            enc_text += i
    return enc_text    

def decr_EN(text, step):
    decr_text = ''
    for i in text:
        if i in en_alpha_0:
            decr_text += en_alpha_0[abs((en_alpha_0.index(i) - step) % 26)]
        elif i in en_alpha_1:
            decr_text += en_alpha_1[abs((en_alpha_1.index(i) - step) % 26)]
        else:
            decr_text += i
    return decr_text

while again.lower() == 'y':
    text = input('Введите текст \n')
    direction = input('Выберите действие: Зашифровать (c) или Расшифровать (d) \n')
    language = input('Выберите язык алфавита: Русский (ru) или Английский (en) \n')
    step = int(input('Укажите шаг сдвига \n'))
    if direction.lower() == 'c' and language.lower() == 'ru':
        print(encr_RU(text, step))
    elif direction.lower() == 'd' and language.lower() == 'ru':
        print(decr_RU(text, step))
    elif direction.lower() == 'c' and language.lower() == 'en':
        print(encr_EN(text, step))
    elif direction.lower() == 'd' and language.lower() == 'en':
        print(decr_EN(text, step))
    else:
        print('Ошибка. Повторите ввод данных')
        continue    
    again = input(f'\nМожет еще один шифр? y/n? ')
    if again.lower() != 'y':
        print(f'\nВозвращайся, если еще нужен шифр!')