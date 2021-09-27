import random

def get_words_list():
    words_list = []
    with open('data.txt', 'r', encoding='utf=8') as f:
        for line in f:
            words_list.append(line)
    return words_list


def get_secret_word():
    return random.choice(get_words_list())


def run():
    secret_word = get_secret_word()
    print(secret_word)


if __name__ == '__main__':
    run()
