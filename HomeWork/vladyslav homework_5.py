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


def recommendation(input_dict: dict) -> tuple:
    second_dict = input_dict.copy()  # Создаю второй dict через копи для проверки каждого с каждым
    name_and_recommendations: list = []  # Имя и рекомендации для каждого пользователя
    return_tuple: tuple = ()  # tuple Для возвращения значения
    good_recommendation: set = set()  # set для будущих рекомендаций
    compared_account: str = list(friends_list)[-1]  # Получаю ключ последнего элемента в input_dict
    соmparable_set: set = friends_list.get(compared_account)  # Получаю значение черещ ключ с последнего значения
    for keys_first_dict in input_dict:  # Цикл для проверки совпадений по значению из input_dict
        set_for_compare = input_dict.get(keys_first_dict)  # значение для сравнения в первом цикле
        for keys_second_dict in second_dict:
            if соmparable_set == second_dict.get(keys_second_dict):  # Проверка на тот же аккаунт
                continue
            compare_result = соmparable_set & second_dict.get(keys_second_dict)  # Найти общих друзей
            if len(compare_result) >= 2:  # Если их больше двух, то записать значение в set
                good_recommendation.add(keys_second_dict)
        name_and_recommendations.append(compared_account)  # добавляю в list имя чел. кому производится рекомендация
        name_and_recommendations.append(good_recommendation)  # множество имен тех кого рекомендуют для подписки
        # print(f'{name_and_recommendations=}')  # Дебаг значения после присваивания
        return_tuple = return_tuple + tuple(name_and_recommendations)  # добавления списка tupl'ов
        name_and_recommendations = []  # Очистка list'a для последущих проверок
        # print(f'{return_tuple=}')  # Дебаг значения после присваивания
        good_recommendation = set()  # Очистка set'a для последущих проверок
        соmparable_set = set_for_compare  # переназначение set'a для сравнения
        compared_account = keys_first_dict  # назначение следующего аккаунта для сравнения
    return return_tuple


print(recommendation(friends_list))


# 2.0 Создать функцию которая принимает неизвестное количество позиционных аргументов, но больше одного.
# В качестве аргументов ожидайте int. Функция должна вернуть сумму этих аргументов
def sum_of_inputs(*args):
    total = 0
    for items in args:
        total += items
    return total

# 3) Написать функцию которая в качестве аргумента принимает словарь, в котором:
# в качестве ключей — числа „int“ а в качестве значений — либо словарь, с такой же структурой, либо None.
# Функция должна вернуть максимально большое число находящееся в этом словаре на произвольной глубине.
