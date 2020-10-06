string: str = 'If I look back I am lost'


def count_char(string_come: str, char_rec: str):
    counter: int = 0
    match_count: int = 0
    while counter < len(string_come):
        temp_char: str = string_come[counter]
        if temp_char == char_rec:
            match_count += 1
        counter += 1
    return match_count


print(count_char(string, 't'))
