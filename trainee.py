string: str = 'If I look back I am lost'


def count_char(string, char):
    index = len(string) - 1
    result = 0
    while index >= 0:
        if string[index] == char:
            result += 1
        index -= 1
    return result


print(count_char(string, 'f'))