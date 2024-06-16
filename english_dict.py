DICT_FILE = 'words_alpha.txt'

def get_all_n_letters_words(n):
    with open(DICT_FILE, 'r') as f:
        lines = f.readlines()
    lines = [line[:-1] for line in lines] # remove newline char
    return [word for word in lines if len(word) == n]
