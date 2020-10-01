matrix = [['   ', '   ', '   ', '   ', '   '],
          ['   ', '   ', '   ', '   ', '   '],
          ['   ', '   ', '   ', '   ', '   '],
          ['   ', '   ', '   ', '   ', '   '],
          ['   ', '   ', '   ', '   ', '   ']]

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


# Прорисовка матрицы
def list_print():
    print(f'\n+{SEPARATOR}+{SEPARATOR}+{SEPARATOR}+{SEPARATOR}+{SEPARATOR}+')
    for x in matrix:
        print(end='|')
        for y in x:
            print(y, end='|')
        # print()
        print(f'\n+{SEPARATOR}+{SEPARATOR}+{SEPARATOR}+{SEPARATOR}+{SEPARATOR}+')


# Перезапись ячейки
def rewrite_value(x_coordinate: int, y_coordinate: int, value_input: str):
    while True:
        if matrix[x_coordinate][y_coordinate] != '   ':
            change_or_not: str = input('Ячейка занята! Перезаписать? \n1) Да.\n2) НЕТ!')
            if change_or_not == "Да.":
                matrix[x_coordinate][y_coordinate] = f' {value_input} '
                print(VALUE_WRITTEN)
                break
            elif change_or_not == 'НЕТ!':
                break


# Проверка значения в ячейке
def check_for_value(x_coordinate: int, y_coordinate: int):
    if matrix[x_coordinate][y_coordinate] != '   ':
        print(matrix[x_coordinate][y_coordinate])
        return
    else:
        print('Ячейка пуста')


def put_empty_value(x_coordinate: int, y_coordinate: int):
    matrix[x_coordinate][y_coordinate] = f'   '
    print(VALUE_WRITTEN)
    return



list_print()  # первоначальный вывод таблицы
user_selected: int = main_menu()  # первоначальное меню
while True:
    # 3.1 --> Запись значения в ячейку
    if user_selected == 1:  #
        coordinates_and_value: str = input('Введите x и y в формате x=1;y=1;value="v"')
        x_coors: int = int(coordinates_and_value[2])  # Чтение координаты X
        y_coors: int = int(coordinates_and_value[6])  # Чтение координаты Y
        value: str = coordinates_and_value[15]  # Чтение записываемого значение
        rewrite_value(x_coors, y_coors, value)  # Передача значений в ответствунную функцию
        user_selected = main_menu()
    # 3.2 --> Проверка значения в ячейке
    elif user_selected == 2:
        coordinates_and_value: str = input('Введите x и y в формате x=1;y=1;')
        x_coors: int = int(coordinates_and_value[2])
        y_coors: int = int(coordinates_and_value[6])
        check_for_value(x_coors, y_coors)
        user_selected = main_menu()
    # 3.3 --> Выводит на экран все ячейки как в самом начале, но с теми значениями, которые пользователь внес в табличку
    elif user_selected == 3:
        list_print()
        user_selected = main_menu()
    # 3.4 --> Записывает пустое значение в ячейку
    elif user_selected == 4:
        coordinates_and_value: str = input('Введите x и y в формате x=1;y=1;')
        x_coors: int = int(coordinates_and_value[2])
        y_coors: int = int(coordinates_and_value[6])
        put_empty_value(x_coors, y_coors)
        user_selected = main_menu()
    elif user_selected == 0:  # 4 --> Выход с программы
        break
else:
    print(f'Неверное значение, пожалуйста повторите ввод')
    user_selected = main_menu()
