some_collection = list(range(20))


# Цикл по коллекциям ИЛИ с использованием итераторов

for elem in some_collection:  # Для каждого элемента (elem) в коллекции (some_collection)
    print(elem)               # Выполнить действие
else:
    print('Закончили без прерывания')

# some_collection - может быть любая коллекция
# блок else не обязателен
# возможно использовать break и continue

# Примеры перемещения по коллекциям с помощью цикла
list_of_tuple = [('сегодня', 'солнечено'), ('вчера', 'пасмурно')]
for key, value in list_of_tuple:  # Элементом этой коллекции является tuple, и мы можем распаковать его прям на месте!
    print(key, value)

list_of_tuple = [('сегодня', 'солнечено', 'но мне было весело'), ('вчера', 'пасмурно', 'а мне все равно хорошо')]

for day, value, mood in list_of_tuple:
    # Элементом этой коллекции является tuple,
    # и мы можем распаковать даже тут!
    print(day, value, mood)


list_of_days = ['сегодня', 'вчера', 'завтра']
for i, value in enumerate(list_of_days):
    # Функция enumerate возвращает объект похожий на список кортежей.
    # И каждый элемент этого списка можно распаковать!
   print(i, value)
