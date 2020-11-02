def read():
    print('Введите путь к файлу (откуда):')
    from_way = input()
    with open(from_way, 'r') as initial_file:
        text_storage = initial_file.readlines()
    return text_storage


def write(what_to_write):
    print('Введите путь к файлу (куда):')
    to_way = input()
    with open(to_way, 'a+') as final_file:
        string_to_write = '****\n****\n'.join(what_to_write)
        final_file.write(string_to_write)
        for i in what_to_write:
            final_file.write(i)
    print('Thank for watching')


copied_text = read()
write(copied_text)
