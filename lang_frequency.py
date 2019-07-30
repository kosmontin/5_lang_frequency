import re
import sys
import collections


def load_data(filepath):
    with open(filepath, encoding='utf-8') as file_handler:
        return file_handler.read()


def get_most_frequent_words(content):
    word_counter = 10
    return collections.Counter(
        re.findall(r"[\w']+", content.lower())
    ).most_common(word_counter)


if __name__ == '__main__':
    sys_arg = ''
    if len(sys.argv) > 1:
        sys_arg = sys.argv[1]
        try:
            print(get_most_frequent_words(load_data(sys_arg)))
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
