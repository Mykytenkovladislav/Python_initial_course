first_column: list = [" 0 ", " 1 ", " 2 ", '   ', ' 4 ']
second_column: list = [" y ", " y ", " y ", '   ', ' y ']
third_column: list = [" t ", " t ", " t ", ' t ', ' t ']
fourth_column: list = [" h ", " h ", " h ", ' h ', ' h ']
fifth_column: list = [" o ", " o ", " o ", ' o ', ' o ']
INPUT_1: str = '1) Сделать запись'
INPUT_2: str = '2) Получить значение по координатам'
INPUT_3: str = '3) Показать все ячейки'
INPUT_4: str = '4) Удалить значение по координатам'
INPUT_0: str = '0) Завершить работу'
SEPARATOR: str = '---'
VALUE_WRITTEN: str = 'Запись сделана!'


def main_menu():
    user_input: str = input(f'{INPUT_1}\n{INPUT_2}\n{INPUT_3}\n{INPUT_4}\n{INPUT_0}\n')
    user_input: int = int(user_input)
    return user_input


def list_print():
    for a, b, c, d, e in zip(first_column, second_column, third_column, fourth_column, fifth_column):
        print(f'+{SEPARATOR}+{SEPARATOR}+{SEPARATOR}+{SEPARATOR}+{SEPARATOR}+')
        print(f'|{a}|{b}|{c}|{d}|{e}|')
    print(f'+{SEPARATOR}+{SEPARATOR}+{SEPARATOR}+{SEPARATOR}+{SEPARATOR}+')


def check_for_value(x_coordinate: int, y_coordinate: int, value_for_block: str):
    if x_coordinate == 0:
        first_column.reverse()
        while True:
            print(first_column[y_coordinate])  # TODO delete after debugging
            if first_column[y_coordinate] != '   ':
                change_or_not: str = input('Ячейка занята! Перезаписать? \n1) Да.\n2) НЕТ!')
                if change_or_not == "Да.":
                    print(f'{x_coordinate=}, {y_coordinate=}')  # TODO delete after debugging
                    first_column[y_coordinate] = f' {value_for_block} '
                    first_column.reverse()
                    print(VALUE_WRITTEN)
                    list_print()  # TODO delete after debugging
                    break
                elif change_or_not == 'НЕТ!':
                    break
            else:
                first_column[y_coordinate] = f' {value_for_block} '
                first_column.reverse()
                print(VALUE_WRITTEN)
                break
    elif x_coordinate == 1:
        second_column.reverse()
        while True:
            print(second_column[y_coordinate])  # TODO delete after debugging
            if second_column[y_coordinate] != '   ':
                change_or_not: str = input('Ячейка занята! Перезаписать? \n1) Да.\n2) НЕТ!')
                if change_or_not == "Да.":
                    print(f'{x_coordinate=}, {y_coordinate=}')  # TODO delete after debugging
                    second_column[y_coordinate] = f' {value_for_block} '
                    second_column.reverse()
                    print(VALUE_WRITTEN)
                    list_print()  # TODO delete after debugging
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
            print(third_column[y_coordinate])  # TODO delete after debugging
            if third_column[y_coordinate] != '   ':
                change_or_not: str = input('Ячейка занята! Перезаписать? \n1) Да.\n2) НЕТ!')
                if change_or_not == "Да.":
                    print(f'{x_coordinate=}, {y_coordinate=}')  # TODO delete after debugging
                    third_column[y_coordinate] = f' {value_for_block} '
                    third_column.reverse()
                    print(VALUE_WRITTEN)
                    list_print()  # TODO delete after debugging
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
            print(fourth_column[y_coordinate])  # TODO delete after debugging
            if fourth_column[y_coordinate] != '   ':
                change_or_not: str = input('Ячейка занята! Перезаписать? \n1) Да.\n2) НЕТ!')
                if change_or_not == "Да.":
                    print(f'{x_coordinate=}, {y_coordinate=}')  # TODO delete after debugging
                    fourth_column[y_coordinate] = f' {value_for_block} '
                    fourth_column.reverse()
                    print(VALUE_WRITTEN)
                    list_print()  # TODO delete after debugging
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
            print(fifth_column[y_coordinate])  # TODO delete after debugging
            if fifth_column[y_coordinate] != '   ':
                change_or_not: str = input('Ячейка занята! Перезаписать? \n1) Да.\n2) НЕТ!')
                if change_or_not == "Да.":
                    print(f'{x_coordinate=}, {y_coordinate=}')  # TODO delete after debugging
                    fifth_column[y_coordinate] = f' {value_for_block} '
                    fifth_column.reverse()
                    print(VALUE_WRITTEN)
                    list_print()  # TODO delete after debugging
                    break
                elif change_or_not == 'НЕТ!':
                    break
            else:
                fifth_column[y_coordinate] = f' {value_for_block} '
                fifth_column.reverse()
                print(VALUE_WRITTEN)
                break


list_print()
user_selected: int = main_menu()
while user_selected != 0:
    if user_selected == 1:
        print(f'{user_selected=}')  # TODO Delete after debugging
        x_coors: int = 0
        y_coors: int = 1
        value: str = '!'
        # coordinates_and_value: str = input('Введите x и y в формате x=1;y=1;value="v"')
        # x_coors: int = int(coordinates_and_value[2])
        # y_coors: int = int(coordinates_and_value[6])
        # value: str = coordinates_and_value[12]  # TODO change v index to value
        print(f'{x_coors=}, {y_coors=}, {value=}')  # TODO Delete after debugging
        check_for_value(x_coors, y_coors, value)
        user_selected = main_menu()
    elif user_selected == 2:
        print(f'{user_selected=}')  # TODO Delete after debugging
        user_selected = main_menu()
    # 3.3 -->Выводит на экран все ячейки как в самом начале, но с теми значениями, которые пользователь внес в табличку
    elif user_selected == 3:
        list_print()
        user_selected = main_menu()
    elif user_selected == 4:
        print(f'{user_selected=}')  # TODO Delete after debugging
        user_selected = main_menu()
else:
    print(f'{user_selected=}')
    user_selected = main_menu()
