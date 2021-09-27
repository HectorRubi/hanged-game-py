import os
import random

def get_words_list():
    words_list = []
    with open('data.txt', 'r', encoding='utf=8') as f:
        for line in f:
            words_list.append(line)
    return words_list


def get_secret_word():
    return random.choice(get_words_list())


def get_secret_word_to_compare(secret_word):
    secret_word_compare = list(enumerate(secret_word))
    del secret_word_compare[-1]
    return secret_word_compare


def get_letter_positions(letter, secret_word):
    return [index for index, char in enumerate(secret_word) if char == letter]


def run():
    has_win = False
    secret_word = get_secret_word()
    secret_word_compare = get_secret_word_to_compare(secret_word)
    word_state = ['_' for i in range(0, len(secret_word) - 1)]

    while(has_win == False):
        print('¡Adivina la palabra!')
        print(*word_state, sep=' ')
        letter = input('Ingresa una letra: ')
        os.system('clear')

        positions = get_letter_positions(letter, secret_word)
        if(len(positions) > 0):
            for p in positions:
                word_state[p] = letter

        if list(enumerate(word_state)) == secret_word_compare:
            has_win = True
            print('Has ganado!')
            print('La palabra era: ')
            print(secret_word)


if __name__ == '__main__':
    run()
