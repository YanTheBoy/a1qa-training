import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('file_path', help='Путь к txt файлу.')
    parser.add_argument('start_string', help='Начальная строка')
    parser.add_argument('final_string', help='Конечная строка')
    return parser.parse_args()


def cut_and_get_string(path, string_from, string_to):
    with open(path, 'r', encoding='utf8') as file:
        lines = file.read().rstrip().split('\n')
        removed_strings = []
        offset = 0
        for number in range(string_from-1, string_to):
            string_num = number-offset
            removed_strings.append(lines[string_num])
            del lines[string_num]
            offset += 1
    return {
        'updated_strings': lines,
        'deleted_strings': removed_strings}


def rewrite_text_file(new_file):
    with open('file.txt', 'w', encoding='utf8') as file:
        for new_string in new_file:
            file.write(new_string+'\n')


if __name__ == '__main__':
    filepath = parse_args().file_path
    start_str = int(parse_args().start_string)
    final_str = int(parse_args().final_string)

    strings = cut_and_get_string(filepath, start_str, final_str)
    for string in strings['deleted_strings']:
        print(string)
    rewrite_text_file(strings['updated_strings'])
