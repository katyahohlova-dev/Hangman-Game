import random 

def get_world():
    with open('words.txt', 'r') as file:
        line = file.readlines()
    words = [word for line in line for word in line.split()]
    random_world = random.choice(words)
    return random_world


def drew(mistake):
    
    HANGMANPICS = (r"""  
            +---+
            |   |
            O   |
           /|\  |
           / \  |
                |
            ========= """, r"""  
            +---+
            |   |
            O   |
           /|\  |
           /    |
                |
            ========= """, r""" 
            +---+
            |   |
            O   |
           /|\  |
                |
                |
            ========= """, r""" 
            +---+
            |   |
            O   |
           /|   |
                |
                |
            ========= """, r"""  
            +---+
            |   |
            O   |
            |   |
                |
                |
            ========= """, r""" 
            +---+
            |   |
            O   |
                |
                |
                |
            ========= """ , r""" 
            +---+
            |   |
                |
                |
                |
                |
            ========= """, r"""
            +---+ 
                |
                |
                |
                |
                |
            ========= """ 
        )
    
    print(HANGMANPICS[mistake])

max_wrong = 7 #всего попыток для разгадывания слова


def main(): #новая игра

    while True: 

        print(
        """
        Команды игры 'Висилица':
        0 - Выйти
        1 - Начать новую игру
        """
        )

        used = [] #использованные буквы
        input_choice = input("Ваш выбор: ")
        
        match input_choice:
            case '0': 
                print('Bye!')
                return 
            case '1':
                
                random_world = get_world()
                
                hidden_world = ['_' for _ in range(len(random_world))]

                print("Добро пожаловать в игру 'Висилица'.")
                print(f'Загаданное слово：{' '.join(hidden_world)}')
                print(f'У тебя всего попыток {max_wrong}')
                
                check_letter(random_world, hidden_world, used)
            case _:
                print('Извините, в меню нет данного пункта. Пожалуйста, попробуйте снова.')
                continue 
            

def show_result(curr_wrong, used, hidden_world, random_world): #отображение промежточного результата
    drew(max_wrong - curr_wrong)
    print(f'Вы отгадали следующие буквы:\n{hidden_world}')
    print(f'Введенные буквы: {', '.join(used)}')
    print(f'Ошибки: {curr_wrong}')

    if curr_wrong < max_wrong and ''.join(random_world) != ''.join(hidden_world):
        return False
    elif random_world==''.join(hidden_world):
        print(f'Поздравляем, ты победил! У тебя осталось {max_wrong-curr_wrong} неизрасходанных попыток')
        return True
    else:
        print('Упс.. Игра окончена.')
        print(f'Загаданное слово было следующим: {''.join(random_world)}')
        return True
    

def check_used(letter, used): #проверка буквы в списке введенных букв 
    if letter not in used:
        used.append(letter) 
        return True 
    else:
        print(f'Данная буква уже использовалась: {','.join(used)}')
        return False
    

def check_letter(random_world, hidden_world, used): #проверка наличия буквы в слове 
    curr_wrong = 0
    word_list = list(random_world)

    while True:
        letter = input('Введите букву: ').lower().strip()
        if len(letter) != 1 or not letter.isalpha():
            print('Неверный ввод')
            continue

        if not check_used(letter, used):
            continue

        if letter in word_list:
            for i in range(len(word_list)):
                if  word_list[i] == letter:
                    hidden_world[i] = letter
                    word_list[i] = '_' #замена отгаданной буквы на _
        else:
            curr_wrong += 1
        
        if show_result(curr_wrong, used, hidden_world, random_world):
            break

if __name__ == '__main__':
    main()
    




