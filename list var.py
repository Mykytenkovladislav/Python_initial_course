matrix = {
    (0, 0): '', (0, 1): '', (0, 2): '', (0, 3): '', (0, 4): '',
    (1, 0): '', (1, 1): '', (1, 2): '', (1, 3): '', (1, 4): '',
    (2, 0): '', (2, 1): '', (2, 2): '', (2, 3): '', (2, 4): '',
    (3, 0): '', (3, 1): '', (3, 2): '', (3, 3): '', (3, 4): '',
    (4, 0): '', (4, 1): '', (4, 2): '', (4, 3): '', (4, 4): '',

}
INPUT_1: str = '1) Сделать запись'
INPUT_2: str = '2) Получить значение по координатам'
INPUT_3: str = '3) Показать все ячейки'
INPUT_4: str = '4) Удалить значение по координатам'
INPUT_0: str = '0) Завершить работу'
SEPARATOR: str = '---'
VALUE_WRITTEN: str = 'Запись сделана!'


# Главное меню
def main_menu():
    user_input: str = input(f'{INPUT_1}\n{INPUT_2}\n{INPUT_3}\n{INPUT_4}\n{INPUT_0}\n')
    user_input: int = int(user_input)
    return user_input


def list_print():
    for x, y in matrix:
        print(f'+{SEPARATOR}+{SEPARATOR}+{SEPARATOR}+{SEPARATOR}+{SEPARATOR}+')
        print(
            f'|{matrix[x, y]}|{matrix[x + 1, y + 1]}|{matrix[x + 1, y + 1]}|{matrix[x, y + 3]}|{matrix[x + 3, y + 3]}|')
        x = x + 1
    print(f'+{SEPARATOR}+{SEPARATOR}+{SEPARATOR}+{SEPARATOR}+{SEPARATOR}+')


list_print()
