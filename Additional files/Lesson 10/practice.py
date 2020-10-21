import math

month_dict = {
    1: 'Winter',
    2: 'Winter',
    3: 'Spring',
    4: 'Spring',
    5: 'Spring',
    6: 'Summer',
    7: 'Summer',
    8: 'Summer',
    9: 'Autumn',
    10: 'Autumn',
    11: 'Autumn',
    12: 'Winter'
}


# task 1
def square(side: int) -> int:
    perimeter = round(side * 4)
    area = round(side * side)
    diagonal = round(math.sqrt((side ** 2 * 2)))
    return perimeter, area, diagonal


print(square(float(input('Введите сторону квадрата: '))))


# Task 2
def seasons(month: int):
    return month_dict.get(month)


print(seasons(int(input('Введите месяц: '))))


# Task 3
def sorting_list(list_1: list, list_2: list) -> list:
    sorted_list: list = []
    for i, k in zip(list_1, list_2):
        sorted_list.append(i)
        sorted_list.append(k)
    return sorted_list


list_temp1 = [1, 2, 3]
list_temp2 = [11, 22, 33]

print(sorting_list(list_temp1, list_temp2))


# task 4
def palindrome_check(user_input: str) -> bool:
    temp = list(user_input)
    print(temp)  # debug
    while len(temp) > 0:
        if len(temp) == 0 or len(temp) == 1:
            return True
        if temp[0] == temp[-1]:
            temp = temp[1:-1]
            print(temp)
        else:
            return False


PALINDROME = 'deified'
print(palindrome_check(PALINDROME))
NOT_PALINDROME = 'deiabgied'
print(palindrome_check(NOT_PALINDROME))

# decorator task
PALINDROME = 'deified'
NOT_PALINDROME = 'deiabgied'


def executing_time(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'[*] Время выполнения: {format(end - start)} секунд.')
        return result

    return wrapper


@executing_time
def palindrome_check(user_input: str) -> bool:
    temp = list(user_input)
    while len(temp) > 0:
        if len(temp) == 0 or len(temp) == 1:
            return True
        if temp[0] == temp[-1]:
            temp = temp[1:-1]
            print(temp)
        else:
            return False


temp1 = palindrome_check(PALINDROME)
temp2 = palindrome_check(NOT_PALINDROME)
print(temp1)
print(temp2)
