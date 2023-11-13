import random

word_list = ['канат', 'барашек', 'дирижабль', 'папка', 'халат', 'щел', 'звездочет', 'барак', 'конвоир', 'квант', 'анчоус', 'дворец', 'будка', 'адъютант', 'метка', 'файл', 'мяс', 'буйвол', 'полиграф', 'еда', 'ремень', 'алмазник', 'бюро', 'жаворонок' 'локоть', 'врач', 'акваланг', 'кастелянша', 'автобаза', 'графин', 'кочка', 'композиция', 'доза', 'кафедра', 'дыба', 'горилла', 'биополе', 'газопровод', 'булавка', 'князь', 'агат', 'кисель', 'дерево', 'лифчик', 'луна', 'корсет', 'зелье', 'кобыла', 'треугольник', 'колбаса', 'альманах', 'зазор', 'томат', 'директор', 'конверт', 'апельсин', 'автопокрышка', 'фосфор', 'плов', 'коммуналка', 'грифон', 'заклепка', 'сабля', 'актив', 'зубр', 'конюшня', 'рюкзак', 'карат', 'фельдшер', 'клапан', 'уксус', 'возница', 'кольчуга', 'шляпа', 'зуб', 'фура', 'мазь', 'платье', 'парус', 'автобус', 'кимоно', 'труба', 'конвейер', 'барометр', 'кокаин', 'пеликан', 'пароль', 'авиабилет', 'защелка', 'табурет', 'шоссе', 'шашка', 'кобель', 'павлин']

def get_word():
    return random.choice(word_list).upper()


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]
    
def play(word):
    word_completion = word[0] +'_' * len(word[1:-1]) + word[-1]
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print('Давайте играть в угадайку слов!')
    print(display_hangman(tries))
    print(f'Слово состоит из {len(word)} букв: {word_completion}')
    while guessed == False:
        print('=================================================')
        print(f'На данный момент вами введены следующие буквы: {guessed_letters} и слова: {guessed_words}')
        print(f'Ваш прогресс: {word_completion}')
        n = input(f'Введите букву или слово: ').upper()
        word = word.upper()
        if n.isalpha():
            if n not in guessed_letters and n not in guessed_words:
                if n == word:
                    print(f'Поздравляем, вы угалади слово! Вы победили! Это {word}')
                    guessed = True
                    
                elif n in word:
                    guessed_letters += n
                    for i in range(len(word)):
                        if word[i] == n:
                            word_completion = word_completion[:i] + n + word_completion[i + 1:]
                            print(f'Угадали!', word_completion)
                            if word_completion == word:
                                print(f'Поздравляем, вы угалади слово! Вы победили! Это {word}')
                                guessed = True
                else:
                    tries -= 1
                    if tries > 0:
                        print(f'Вы не угадали! Осталось попыток: {tries} ')
                        print(display_hangman(tries))
                        if len(n) == 1:
                            guessed_letters += n
                        elif len(n) > 1:
                            guessed_words.append(n)
                    elif tries == 0:
                        print(f'Вы исчерпали все попытки')
                        print(f'Загаданное слово: {word}')
                        print(display_hangman(tries))
                        break
            else:
                print(f'Вы уже ранее называли {n}. Повторите ввод')
                continue
                
        else:
            print(f'Ошибка! Введите букву русского алфавита')
            continue
        
def process():
    again = 'y'
    while again.lower() == 'y':
        play(get_word())
        again = input(f'\nМожет еще разок? y/n? ')
        if again.lower() != 'y':
            print(f'\nВозвращайся, если захочешь сыграть еще!')
        
process()
        