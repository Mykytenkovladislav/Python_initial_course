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
stop_words: set = set(stopwords.words('english'))
# специальный объект, который будет приводить слова к лемам
lemmatizer = WordNetLemmatizer()

# Воспользуемся встроенной функцией open
dataset_file = open('SMSSpamCollection.txt', mode='r', encoding='utf-8')

# 0 ---------------------------------------------------------------------------------------

# метод объекта файла readlines - возвращает список строк
dataset: list = dataset_file.readlines()
# закрываем файловый дескриптор
dataset_file.close()

random.shuffle(dataset)  # перетасовываем наши данные

# 1 ---------------------------------------------------------------------------------------
spam_dataset: set = set()
ham_dataset: set = set()

for line in dataset:
    temp = line[: 3]
    if line.startswith('spam\t'):
        line_for_append = line.replace('spam\t', '')
        spam_dataset.add(line_for_append)
    elif line.startswith('ham\t'):
        line_for_append = line.replace('ham\t', '')
        ham_dataset.add(line_for_append)
# 2 ---------------------------------------------------------------------------------------

spam_dataset_test: set = set(
    random.sample(spam_dataset, int(len(spam_dataset) * 0.2))
)
spam_dataset_main: set = spam_dataset.difference(spam_dataset_test)

ham_dataset_test: set = set(
    random.sample(ham_dataset, int(len(ham_dataset) * 0.2))
)
ham_dataset_main: set = ham_dataset.difference(ham_dataset_test)


# 3 ---------------------------------------------------------------------------------------

def processing_dataset(dataset: set) -> dict:
    word_dataset = []
    for line in dataset:
        line = re.sub(r'[A-Za-z ]', '', line)  # Оставляет пробелы и все буквы, остальное удаляет
        line.lower()
        line_words: list = line.split()
        line_words = list(
            [lemmatizer.lemmatize(word) for word in line_words if word not in stop_words]
        )  # высчитываем лему
        word_dataset += line_words

    word_counter = Counter(word_dataset)

    # теперь можем узнать частоту встречаемости разных слов
    len_word_dataset = len(word_dataset)
    result_dict = {}
    for key, count in word_counter.items():
        result_dict[key] = count / len_word_dataset
    return result_dict


print(f'count of spam sms for analysis:  {len(spam_dataset_test)}')
print(f'count of ham sms for analysis:  {len(ham_dataset_test)}')

ham_words = processing_dataset(ham_dataset_main)
spam_words = processing_dataset(spam_dataset_main)

# 4 ---------------------------------------------------------------------------------------

learning_result: dict = {}
learning_result_keys: list = list(spam_words.keys()) + list(ham_words.keys())

for key in learning_result_keys:
    in_spam_word = spam_words.get(key, 0) > ham_words.get(key, 0)
    in_ham_word = spam_words.get(key, 0) > ham_words.get(key, 0)
