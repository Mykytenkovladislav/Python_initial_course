first_column: list = ["   ", "   ", "   ", '   ', '   ']  # Я использовал '   '
second_column: list = ["   ", "   ", "   ", '   ', '   ']  # вместо '' для красивой таблички в начале
third_column: list = ["   ", "   ", "   ", '   ', '   ']
fourth_column: list = ["   ", "   ", "   ", '   ', '   ']
fifth_column: list = ["   ", "   ", "   ", '   ', '   ']
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
    for a, b, c, d, e in zip(first_column, second_column, third_column, fourth_column, fifth_column):
        print(f'+{SEPARATOR}+{SEPARATOR}+{SEPARATOR}+{SEPARATOR}+{SEPARATOR}+')
        print(f'|{a}|{b}|{c}|{d}|{e}|')
    print(f'+{SEPARATOR}+{SEPARATOR}+{SEPARATOR}+{SEPARATOR}+{SEPARATOR}+')


# Функция для записи в ячейку с проверкой занята она или нет
def rewrite_value(x_coordinate: int, y_coordinate: int, value_for_block: str):
    if x_coordinate == 0:
        first_column.reverse()  # Для правильного выбора по координате Y, оставлю этот коммент только один раз, т.к.
        while True:  # дальше смысл один и тот же. P.S Если надо повторно написать везде, дай знать
            if first_column[y_coordinate] != '   ':  # TODO уточнить у Егора при "" в знач можно bool=False?
                change_or_not: str = input('Ячейка занята! Перезаписать? \n1) Да.\n2) НЕТ!')
                if change_or_not == "Да.":
                    first_column[y_coordinate] = f' {value_for_block} '
                    first_column.reverse()  # Возврат к нормальному виду
                    print(VALUE_WRITTEN)
                    break
                elif change_or_not == 'НЕТ!':  # возврат к главному менб
                    break
            else:  # Если пустое, то записываем
                first_column[y_coordinate] = f' {value_for_block} '
                first_column.reverse()  # Возврат к нормальному виду
                print(VALUE_WRITTEN)
                break
    elif x_coordinate == 1:
        second_column.reverse()
        while True:
            if second_column[y_coordinate] != '   ':
                change_or_not: str = input('Ячейка занята! Перезаписать? \n1) Да.\n2) НЕТ!')
                if change_or_not == "Да.":
                    second_column[y_coordinate] = f' {value_for_block} '
                    second_column.reverse()
                    print(VALUE_WRITTEN)
                    break
                elif change_or_not == 'НЕТ!':
                    break
            else:
                second_column[y_coordinate] = f' {value_for_block} '
                second_column.reverse()
                print(VALUE_WRITTEN)
                break
    elif x_coordinate == 2:
        third_column.reverse()
        while True:
            if third_column[y_coordinate] != '   ':
                change_or_not: str = input('Ячейка занята! Перезаписать? \n1) Да.\n2) НЕТ!')
                if change_or_not == "Да.":
                    third_column[y_coordinate] = f' {value_for_block} '
                    third_column.reverse()
                    print(VALUE_WRITTEN)
                    break
                elif change_or_not == 'НЕТ!':
                    break
            else:
                third_column[y_coordinate] = f' {value_for_block} '
                third_column.reverse()
                print(VALUE_WRITTEN)
                break
    elif x_coordinate == 3:
        fourth_column.reverse()
        while True:
            if fourth_column[y_coordinate] != '   ':
                change_or_not: str = input('Ячейка занята! Перезаписать? \n1) Да.\n2) НЕТ!')
                if change_or_not == "Да.":
                    fourth_column[y_coordinate] = f' {value_for_block} '
                    fourth_column.reverse()
                    print(VALUE_WRITTEN)
                    break
                elif change_or_not == 'НЕТ!':
                    break
            else:
                fourth_column[y_coordinate] = f' {value_for_block} '
                fourth_column.reverse()
                print(VALUE_WRITTEN)
                break
    elif x_coordinate == 4:
        fifth_column.reverse()
        while True:
            if fifth_column[y_coordinate] != '   ':
                change_or_not: str = input('Ячейка занята! Перезаписать? \n1) Да.\n2) НЕТ!')
                if change_or_not == "Да.":
                    fifth_column[y_coordinate] = f' {value_for_block} '
                    fifth_column.reverse()
                    print(VALUE_WRITTEN)
                    break
                elif change_or_not == 'НЕТ!':
                    break
            else:
                fifth_column[y_coordinate] = f' {value_for_block} '
                fifth_column.reverse()
                print(VALUE_WRITTEN)
                break
    else:
        print('Введённый координаты не верны. Возврат к меню выбора!')


# Функция для проверки значения в определённой ячейке
def check_for_value(x_coordinate: int, y_coordinate: int):
    if x_coordinate == 0:
        first_column.reverse()
        if first_column[y_coordinate] != '   ':  # TODO уточнить у Егора при "" в знач можно bool=False?
            print(first_column[y_coordinate])
            first_column.reverse()
            return
        else:
            print('Ячейка пуста')
            first_column.reverse()
    elif x_coordinate == 1:
        second_column.reverse()
        if second_column[y_coordinate] != '   ':  # TODO уточнить у Егора при "" в знач можно bool=False?
            print(second_column[y_coordinate])
            second_column.reverse()
            return
        else:
            print('Ячейка пуста')
            second_column.reverse()
    elif x_coordinate == 2:
        third_column.reverse()
        if third_column[y_coordinate] != '   ':  # TODO уточнить у Егора при "" в знач можно bool=False?
            print(third_column[y_coordinate])
            third_column.reverse()
            return
        else:
            print('Ячейка пуста')
            third_column.reverse()
    elif x_coordinate == 3:
        fourth_column.reverse()
        if fourth_column[y_coordinate] != '   ':  # TODO уточнить у Егора при "" в знач можно bool=False?
            print(fourth_column[y_coordinate])
            fourth_column.reverse()
            return
        else:
            print('Ячейка пуста')
            fourth_column.reverse()
    elif x_coordinate == 3:
        fifth_column.reverse()
        if fifth_column[y_coordinate] != '   ':  # TODO уточнить у Егора при "" в знач можно bool=False?
            print(fifth_column[y_coordinate])
            fifth_column.reverse()
            return
        else:
            print('Ячейка пуста')
            fifth_column.reverse()
    else:
        print('Введённый координаты не верны. Возврат к меню выбора!')


def put_empty_value(x_coordinate: int, y_coordinate: int):
    if x_coordinate == 0:
        first_column.reverse()
        print(first_column[y_coordinate])
        first_column[y_coordinate] = f'   '
        first_column.reverse()
        print(VALUE_WRITTEN)
        return
    elif x_coordinate == 1:
        second_column.reverse()
        print(second_column[y_coordinate])
        second_column[y_coordinate] = f'   '
        second_column.reverse()
        print(VALUE_WRITTEN)
        return
    elif x_coordinate == 2:
        third_column.reverse()
        print(third_column[y_coordinate])
        third_column[y_coordinate] = f'   '
        third_column.reverse()
        print(VALUE_WRITTEN)
        return
    elif x_coordinate == 3:
        fourth_column.reverse()
        print(fourth_column[y_coordinate])
        fourth_column[y_coordinate] = f'   '
        fourth_column.reverse()
        print(VALUE_WRITTEN)
        return
    elif x_coordinate == 4:
        fifth_column.reverse()
        print(fifth_column[y_coordinate])
        fifth_column[y_coordinate] = f'   '
        fifth_column.reverse()
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
    elif user_selected == 3:  # 3.3 условие, ввод = 3
        list_print()
        user_selected = main_menu()
    # 3.4 --> Записывает пустое значение в ячейку
    elif user_selected == 4:  # 3.4 условие, ввод = 4
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
