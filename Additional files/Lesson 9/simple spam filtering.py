import random
import re
import nltk
from collections import Counter
from nltk.stem import WordNetLemmatizer

from nltk.corpus import stopwords

# Необходимо подгрузить некоторые данные, такие как список служебных слов.
nltk.download('stopwords')
nltk.download('wordnet')
# множество служебных слов
stop_words = set(stopwords.words('english'))
# специальный объект, который будет приводить слова к лемам
lemmatizer = WordNetLemmatizer()

# Нам известно, что наш датасет - состоит из строк, разделенных \n,
# Внутри которых у нас есть КЛАСС (ham/spam), после которого идет знак \t
# и текст сообщения. \
# Кодировка файла - utf8.

# Воспользуемся встроеной функцией open
dataset_file = open("SMSSpamCollection.txt", encoding='utf-8')

# 0 ---------------------------------------------------------------

# метод объекта файла readlines - возвращает список строк.
dataset: list = dataset_file.readlines()
# закрываем файловый дескриптор
dataset_file.close()

random.shuffle(dataset)  # перетасовываем наши данные.

# 1 ---------------------------------------------------------------

# Разделим наш датасет (spam/ham) на два датасета.
# Напишите свою реализацию разделения одного датасета на два раздельных -
# 1)spam; 2)ham;

spam_dataset: set = set()
ham_dataset: set = set()
for line in dataset:
    if line.startswith('spam\t'):
        line_for_append = line.replace('spam\t', '')
        spam_dataset.add(line_for_append)
    elif line.startswith('ham\t'):
        line_for_append = line.replace('ham\t', '')
        ham_dataset.add(line_for_append)

# 2 ---------------------------------------------------------------
# Теперь, в лучших традициях машинного обучения,
# мы должны разделить наши данные на две подгруппы для кажого сета:
# - Данные на которых будет происходить 'Обучение' нашего 'наивного байеса'
# (зачастую используют 80% от полного сета)
# - Данные на которых мы будем проверять качество работы нашего алгоритма
# (зачастую используют 20% от полного сета)


# воспользуемся опять модулем random
# функция sample вернет новый list элементов,
# состоящий из рандомных элементов первого аргумента, длиной n (второй аргумент)
spam_dataset_test: set = set(
    random.sample(spam_dataset, int(len(spam_dataset) * 0.2))
)
# разница множеств общего спам-сета и тестового спам-сета - это и будет наш
spam_dataset_main: set = spam_dataset.difference(spam_dataset_test)

ham_dataset_test: set = set(
    random.sample(ham_dataset, int(len(ham_dataset) * 0.2))
)
ham_dataset_main: set = ham_dataset.difference(ham_dataset_test)


# 3 ---------------------------------------------------------------

# пожалуй теперь, нам стоит задуматься над обработкой наших данных.
# 0) Полчуим вместо списка сообщений, список всех слов
# 1) Преобразуем все слова к нижнему регистр
# 3) Удалим служебные слова (предлоги, союзы, частицы)
# 4) Проведем лемматизацию всех слов (получим основу слова)


def processing_dataset(dataset: set) -> dict:
    word_dataset = []
    for line in dataset:
        line = re.sub(r'[^A-Za-z ]', '', line)
        # это оставит в нашей строке только буквы и пробелы
        line = line.lower()
        line_words: list = line.split()
        line_words = list(
            [lemmatizer.lemmatize(word) for word in line_words if word not in stop_words]
        )
        word_dataset += line_words

    # Counter - это такая не базовая структура данных, похожая на словарь
    # в нее нужно передовать последовательность, а он вернет структуру очень похожую на 'dict'.
    # в которой в качестве ключей будут элементы последовательности, а в качестве значений -
    # количество их повторений в этой последовательности
    word_counter = Counter(word_dataset)

    # теперь можем узнать частоту встрачаемости разных слов
    len_word_dataset = len(word_dataset)
    result_dict = {}
    for key, count in word_counter.items():
        result_dict[key] = count / len_word_dataset
    return result_dict


print(f'count of spam sms for analysis: {len(spam_dataset_main)=}')
print(f'count of ham sms for analysis: {len(ham_dataset_main)=}')

spam_words = processing_dataset(spam_dataset_main)
ham_words = processing_dataset(ham_dataset_main)

# 4 ---------------------------------------------------------------

# теперь было бы удобно узнать, какие слова чаще встречаються в спам-письмах, а какие в обычных

# Создадим словарь - analysis_result, в котором в качестве ключей будут слова, а в качестве значений - True или False,
# True - если слово чаще встречается в СПАМЕ
# False - если чаще встречается в обычных письмах


learning_result: dict = {}
learning_result_keys: list = list(spam_words.keys()) + list(ham_words.keys())

for key in learning_result_keys:
    is_spam_word = spam_words.get(key, 0) > ham_words.get(key, 0)
    learning_result[key] = is_spam_word


# 5 ---------------------------------------------------------------
# Отлчично! Мы сделали Большую часть работы по созданию модели анализа.
# Теперь пора бы начать ее тестировать. Для этого будем использовать те самые Тест-датасеты.


def analise_test_dataset(dataset_for_analise: set, dataset_type='spam'):
    false_negative_score = 0
    false_positive_score = 0
    dataset_for_analise_len = len(dataset_for_analise)
    for line in dataset_for_analise:
        line = re.sub(r'[^A-Za-z ]', '', line)
        # это оставит в нашей строке только буквы и пробелы
        line = line.lower()
        line_words: list = line.split()
        line_words = list([lemmatizer.lemmatize(word) for word in line_words if word not in stop_words])

        spam_score_for_line = 0
        normal_score = 0
        for word in line_words:
            if learning_result.get(word, False):
                spam_score_for_line += 1
            else:
                normal_score += 1

        mark_as_spam = spam_score_for_line >= normal_score

        if dataset_type == 'spam' and not mark_as_spam:
            false_negative_score += 1
        elif dataset_type == 'ham' and mark_as_spam:
            false_positive_score += 1

    if dataset_type == 'spam':
        print(f'false negative rate: {false_negative_score / dataset_for_analise_len}')
    elif dataset_type == 'ham':
        print(f'false positive rate: {false_positive_score / dataset_for_analise_len}')


analise_test_dataset(spam_dataset_test)
analise_test_dataset(ham_dataset_test, dataset_type='ham')
