import english_dict
import random

WORD = 'basin'
WORD_LEN = 5
assert len(WORD) == WORD_LEN


GRAY = 0
YELLOW = 1
GREEN = 2

all_words = english_dict.get_all_n_letters_words(WORD_LEN)

def getGreenSTR(skk): return "\033[92m {}\033[00m" .format(skk)
def getYellowSTR(skk): return "\033[93m {}\033[00m" .format(skk)
def getLightGraySTR(skk): return "\033[97m {}\033[00m" .format(skk)
color_fn = {GRAY: getLightGraySTR, YELLOW: getYellowSTR, GREEN: getGreenSTR}

def print_guess(guess):
    colored_word = ""
    for i in range(WORD_LEN):
        colored_word += color_fn[guess["res"][i]](guess["word"][i])
    print(colored_word)

letters_history = {chr(i) : GRAY for i in range(97,97+26)}
def print_keyboard():
    keyboard_str = ""
    for letter,val in letters_history.items():
        keyboard_str += color_fn[val](letter)
    print(keyboard_str)


def set_new_word():
    global WORD
    WORD = random.choice(all_words)
    #print(f'new word been set: {WORD}')

def try_word(word):
    word_chars = list(word)
    if len(word) != len(WORD):
        raise Exception('bad word length')
    if word not in all_words:
        raise Exception('word is not in dict')
    res = [None] * WORD_LEN
    for i in range(WORD_LEN):
        if word_chars[i] == WORD[i]:
            res[i] = GREEN
            word_chars[i] = '!'
            letters_history[word[i]] = GREEN

    for i in range(WORD_LEN):
        if word_chars[i] in WORD:
            res[i] = YELLOW
            word_chars[i] = '!'
            letters_history[word[i]] = YELLOW

    for i in range(WORD_LEN):
        if word_chars[i] != '!':
            res[i] = GRAY
    
    assert None not in res

    guess = {'word': word, 'res': res}
    print_guess(guess)
    print_keyboard()
    return guess
