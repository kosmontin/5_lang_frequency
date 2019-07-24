import re
import sys


def load_data(filepath):
    with open(filepath, encoding='utf-8') as file_handler:
        return re.findall(r"[\w']+", file_handler.read().lower())


def get_most_frequent_words(text):
    words_dict = {}
    for word in text:
        if word in words_dict.keys():
            words_dict[word] += 1
        else:
            words_dict[word] = 1
    return sorted(
        words_dict.items(),
        key=lambda value: value[1],
        reverse=True
    )


if __name__ == '__main__':
    sys_arg = ''
    if len(sys.argv) > 1:
        sys_arg = sys.argv[1]
        try:
            for line in get_most_frequent_words(load_data(sys_arg)):
                print(line)
        except FileNotFoundError:
            print('File "', sys_arg, '" not found.', sep='')
    else:
        print(
            '''
            The module calculating most frequent words in present text file.
            For using this module pass text file as argument.
            For example like this:
            lang_frequency.py <text_file.txt>
            '''
        )
