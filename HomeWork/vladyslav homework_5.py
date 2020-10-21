# 1) Написать функцию которая принимает в качестве аргумента принимает структуру данных:
# словарь в котором
# в качестве ключей, имена людей (str),
# в качестве значений — множества (set).
# В множествах находятся имена людей, которые соответствуют подпискам.
# { ‘some_name’: (‘some name1’, ‘some name2’), }
# В этой структуре по ключу мы получаем множество подписок человека.
# Функция должна вернуть список кортежей,
# в которых первый элемент — имя человека которому производиться рекомендация,
# а второй — множество имен тех кого рекомендуют для подписки.
# В рекомендацию стоит добавить имя если, этого имени еще нет в списке подписок,
# при этом как минимум двое из людей на которых человек уже подписан, подписаны на этого человека с этим именем.

friends_list: dict = {  # Debug dict
    "Антон": {"Олег", "Игорь", "Паша", "Филипп"},
    "Георгий": {"Таня", "Настя", "Филипп", "Робокоп"},
    "Настя": {"Тамара", "Игорь", "Антон", "Георгий"},
    "Олег": {"Робокоп", "Робоцып", "Дарт Вейдер", "Антон", "Игорь", "Филипп"}
}


def recommendation(friends_list_: dict) -> list:
    second_dict = friends_list_.copy()  # Создаю второй dict через копи для проверки каждого с каждым
    name_and_recommendations: list = []  # Имя и рекомендации для каждого пользователя
    return_list: list = []  # list Для возвращения значения
    good_recommendation: set = set()  # set для будущих рекомендаций
    compared_account: str = list(friends_list)[-1]  # Получаю ключ последнего элемента в input_dict
    comparable_set: set = friends_list.get(compared_account)  # Получаю значение через ключ с последнего значения
    for keys_first_dict in friends_list_:  # Цикл для проверки совпадений по значению из input_dict
        set_for_compare = friends_list_.get(keys_first_dict)  # значение для сравнения в первом цикле
        for keys_second_dict in second_dict:
            if comparable_set == second_dict.get(keys_second_dict):  # Проверка на тот же аккаунт
                continue
            compare_result = comparable_set & second_dict.get(keys_second_dict)  # Найти общих друзей
            if len(compare_result) >= 2:  # Если их больше двух, то записать значение в set
                if keys_second_dict in comparable_set:  # Проверка на уже наличие в друзьях
                    continue
                good_recommendation.add(keys_second_dict)
        good_recommendation = good_recommendation - set_for_compare
        if good_recommendation != set():  # проверка на пустой сет, что бы не отображать их
            name_and_recommendations.append(compared_account)  # добавляю в list имя чел. кому производится рекомендация
            name_and_recommendations.append(good_recommendation)  # множество имен тех кого рекомендуют для подписки
            return_list.append(tuple(name_and_recommendations))  # добавления списка tuple
            good_recommendation = set()  # Очистка set для последущих проверок
        name_and_recommendations = []  # Очистка list для последущих проверок
        comparable_set = set_for_compare  # переназначение set для сравнения
        compared_account = keys_first_dict  # назначение следующего аккаунта для сравнения
    return return_list


print(recommendation(friends_list))


print(recommendation(friends_list))


# 2.0 Создать функцию которая принимает неизвестное количество позиционных аргументов, но больше одного.
# В качестве аргументов ожидайте int. Функция должна вернуть сумму этих аргументов
def sum_of_inputs(*args) -> int:
    total: int = 0
    for items in args:
        total += items
    return total


print(sum_of_inputs(1, 2, 3, 4, 5, 6, 7, 8, 9, 0))

# 3) Написать функцию которая в качестве аргумента принимает словарь, в котором:
# в качестве ключей — числа „int“ а в качестве значений — либо словарь, с такой же структурой, либо None.
# Функция должна вернуть максимально большое число находящееся в этом словаре на произвольной глубине.

# 3) Написать функцию которая в качестве аргумента принимает словарь, в котором:
# в качестве ключей — числа „int“ а в качестве значений — либо словарь, с такой же структурой, либо None.
# Функция должна вернуть максимально большое число находящееся в этом словаре на произвольной глубине.

input_dict: dict = {  # Для дебага
    2: None,
    4: None,
    12: {
        9: None,
        -8: None,
        547: {
            658: None,
            777: None,
            567: None
        }
    },
    15: None,
    59: {
        9: None,
        12: None,
    }
}


# тут мало чего можно комментировать
def recursive_func(received_dict: dict):
    maximum = received_dict[1]
    for key, value in received_dict.items():
        if key > maximum:
            maximum = key
        if value is not None:
            maximum = recursive_func(value, maximum)
    return maximum


print(recursive_func(input_dict))
