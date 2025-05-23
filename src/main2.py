##
# Created by KatyaHohlova
##

import random
from typing import List, Tuple
from hangman import HANGMANPICS
import re


def draw_status(num_mistakes: int, hangman_pictures: List[str] = HANGMANPICS) -> None:
    print(hangman_pictures[num_mistakes])


def generation_word(filename: str = 'words.txt')-> Tuple[str, List[str]]:
    with open(filename, 'r', encoding='utf-8') as file:
        list_words = list(map(str.strip, file.readlines()))

    random_word = random.choice(list_words)
    hidden_word = ['_' for _ in range(len(random_word))]
    return random_word, hidden_word


def main()-> None:
    while True:
        print(
        """
        Команды игры 'Висилица':
        0 - Выйти
        1 - Начать новую игру
        """
        )

        input_choice = input("Ваш выбор: ")

        match input_choice:
            case '0': 
                print('Bye!')
                return 
            case '1':
                print("Добро пожаловать в игру 'Висилица'.")
                start_game_round()
            case _:
                print("Извините, в меню нет данного пункта. Пожалуйста, попробуйте снова.")
                continue


def validation_letter(letter: str) -> bool:
    return (isinstance(letter, str)
            and len(letter) == 1
            and re.match(r'^[а-яА-Я]+$', letter)
            )


def make_input_letter(used_letters: List[str]) -> str|None:
    while True:
        user_input = input('Введите букву: ').lower().strip()
        if not validation_letter(user_input):
            print('Неккоректный ввод')
            continue

        if  is_letter_used(user_input, used_letters):
            print(f"Данная буква уже использовалась: {','.join(used_letters)}")
            continue

        return user_input


def start_game_loop(random_word: str, hidden_word: List[str], max_wrong: int) -> None:
    used_letters = []
    curr_wrong = 0

    while True:
        input_letter = make_input_letter(used_letters)
        used_letters.append(input_letter)
        if input_letter in random_word:
            open_letter_in_mask(input_letter, random_word, hidden_word)
        else:
            curr_wrong += 1

        game_over, message = check_game_status(random_word, hidden_word, curr_wrong, max_wrong)
        draw_status(max_wrong - curr_wrong)
        show_result(curr_wrong, used_letters, hidden_word)

        if game_over:
            print(message)
            break


def start_game_round()-> None:
    max_wrong = len(HANGMANPICS) - 1
    new_random_word, hidden_random_word = generation_word('words.txt')
    draw_status(max_wrong)
    print(f"Загаданное слово：{' '.join(hidden_random_word)}")
    print(f"Всего попыток: {max_wrong}")
    start_game_loop(new_random_word, hidden_random_word, max_wrong)


def open_letter_in_mask(letter:str, random_word:str, hidden_word:List[str]) -> None:
    word_list = list(random_word)

    for i in range(len(word_list)):
        if word_list[i] == letter:
            hidden_word[i] = letter


def check_game_status(random_word: str, hidden_word: List[str], curr_wrong: int, max_wrong: int) -> Tuple[bool, str]:
    if  random_word == ''.join(hidden_word):
        return True, f"Поздравляем, ты победил! Загаданное слово было следующее: {random_word}"
    if curr_wrong >= max_wrong:
        return True, f"Упс...Игра окончена. Загаданное слово было сдедующее: {random_word}"
    return False, ''


def show_result(curr_wrong: int, used_letters: List[str], hidden_word: List[str]) -> None:
    print(f"Отгаданные буквы:\n{hidden_word}")
    print(f"Введенные буквы: {', '.join(used_letters)}")
    print(f"Ошибки: {curr_wrong}")


def is_letter_used(letter:str, used_letters:List[str]) -> bool:
    return letter in used_letters


if __name__ == '__main__':
    main()