# 2.0 Создать функцию которая принимает неизвестное количество позиционных аргументов, но больше одного.
# В качестве аргументов ожидайте int. Функция должна вернуть сумму этих аргументов
def sum_of_inputs(*args):
    total = 0
    for items in args:
        total += items
    return total


input_for_sum = sum_of_inputs(4, 5, 7, 12)
print(input_for_sum)
