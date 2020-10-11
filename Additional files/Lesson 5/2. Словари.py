#  Словарь - неупорядоченная коллекция пар "ключ: значение"

# Созание словаря
some_dict = {}
capital_cities = dict()

capital_cities = {
    'Ukraine': 'Kiev',
    'USA': 'Washington'
}

capital_cities = dict(Ukraine='Kiev', USA='Washington')

capital_cities = dict([("Russia", "Moscow"), ("Ukraine", "Kiev"), ("USA", "Washington")])

capital_cities['Ukraine'] = 'Kiev'
capital_cities['USA'] = 'Washington'
capital_cities['China'] = 'Beijing'

# Примеры использования
# 1) Посчет объектов  :)
we_had_two_bags_of_ = {
    'pencil': 2,
    'pen': 75,
    'stationery glass': 5,
}
# 2) Установка соответсвия между объектами, например:
# родитель-потомок
family = {
    'mom': 'I',
    'granny': 'mom',
    'great-granny': 'granny'
}

# Как же что-то пложить в словарь?
family['some_key'] = 'some value'

# А как достать значение по ключу?
x = family['some_key']  # Вернет вам значение, а если такого ключа нет, кинет исключение

# Как быть если не знаешь, есть ли там ключ?
# Можно провести проверку, есть ли там этот ключ

is_key_in_dict: bool = 'some_key' in family
# Или можно сделать проще:
x2 = family.get('some_key')  # Вернет значение, а если ключа нет, Вернет None
x3 = family.get('some_key', 'some default value')  # Вернет значение, а если ключа нет, Вернет второй аргумент
x4 = family.setdefault('some_key', 'some_default_value')  # Вернет значение, а если ключа нет,
# Второй аргумент станет этим значением, и будет возвращен

# Другие метод словарей
family.items()  # => [('mom', 'I'), ('granny', 'mom'), ('great-granny', 'granny')] Вернет такую структуру данных
family.keys()  # => ('mom', 'granny', 'great-granny') Вернеет коллекцию ключей
family.values()  # => ('I', 'mom', 'granny') Вернеет коллекцию значений
family.clear()  # => удяляет все элементы

we_had_two_bags_of_.pop('pencil')  # удаляет пару ключ-значение из словаря, возвращая значение
we_had_two_bags_of_.copy()  # Копирует существующий словарь
we_had_two_bags_of_.update({3: 'some'})  # Обновляет текущий словарь, элементами из словаря-аргумента
# При этом, если ключ уже был в словаре, его значение будет заменено на значение новое,
# а если ключа не было, пара ключ-значение просто будет добавлена к словарю


l = ['Погода была супер', None, None, None, 'погода так себе']

z = l[4]

d = {
    (0, 2): 'Погода была супер',
    4: 'погода так себе'
}

y = d[4]
