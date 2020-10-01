# Task 1
INPUT_TASK_1: str = "'(etnfづzxfk｡12dt◕`1ad‿6hns‿1zQY◕Cd$y｡FtSq)Ze6?づ#2)$'\"'"
start: int = 5  # since we need to start at the fifth index
step: int = 5
sorted_string: str = INPUT_TASK_1[start::step]
print(INPUT_TASK_1)  # Original string
print(sorted_string)

# Task 2
INPUT_TASK_2: str = 'some strokа'
PLUS_TO_INDEX: int = 26

# min and max unicode values
min_unicode_value_from_input_task_2: str = min(INPUT_TASK_2)  # ' '
max_unicode_value_from_input_task_2: str = max(INPUT_TASK_2)  # 'а'
print(
    f'Minimal and maximal unicode values:{min_unicode_value_from_input_task_2},{max_unicode_value_from_input_task_2}')

# min and max unicode numbers
min_unicode_number: int = ord(min_unicode_value_from_input_task_2)  # 32
max_unicode_number: int = ord(max_unicode_value_from_input_task_2)  # 1072
print(f'Minimal and maximal unicode number:{str(min_unicode_number)},{str(max_unicode_number)}')

# plus 26 to max unicode number from INPUT_TASK2 and differences between max unicode value and 1004 -->print
print(chr(max_unicode_number + PLUS_TO_INDEX) + ',' + chr(max_unicode_number - 1004))  # 1072+26 and 1072-1004

# Task 3
# Солом названы марсианские солнечные сутки, продолжительность которых равна 24 часам, 39 минутам, 35,244 секундам.
# Напомним, что на Земле средняя продолжительность солнечных суток составляют 24 часа, 3 минуты, 56,5554 секунд.
EARTH_DAY_IN_MINUTES: int = 1443
MARS_DAY_IN_MINUTES: int = 1479

# Separating days and hours
earth_days, earth_hours = input('Enter 2 numbers (separated by a comma and space): ').split(', ')
# converting to int values for math operations
earth_days: int = int(earth_days)
earth_hours: int = int(earth_hours)
# converting to sols
sols: float = (earth_days * EARTH_DAY_IN_MINUTES + earth_hours * 60) / MARS_DAY_IN_MINUTES
sols: float = round(sols, 2)
sols: str = str(sols)
# print with round
print('Sols on Mars:' + sols)

# Task 4
user_input = input('Please, enter your text: ')
# user_input = 'Черт чеРт, Чертополох черта чЕртеж ЧЕРТ начертАно Начертил'
#  text converting to lover case, because the ending case of the text doesn't matter
converted_text = user_input.lower()
# checking all combination of "черт" in text
converted_text = converted_text.replace(' черт ', ' #### ')
converted_text = converted_text.replace(' черт,', ' ####,')
converted_text = converted_text.replace(' черт.', ' ####.')
converted_text = converted_text.replace(' черт:', ' ####: ')
converted_text = converted_text.replace(' черт;', ' ####; ')
# checking "черт" on the start of text
if 'черт ' in converted_text[0: 5]:
    converted_text = converted_text.replace('черт ', ' #### ', 1)
elif 'черт, ' in converted_text[0: 6]:
    converted_text = converted_text.replace('черт,', ' ####,', 1)
elif 'черт. ' in converted_text[0: 6]:
    converted_text = converted_text.replace('черт.', ' ####.', 1)
elif 'черт: ' in converted_text[0: 6]:
    converted_text = converted_text.replace('черт:', ' ####:', 1)
elif 'черт; ' in converted_text[0: 6]:
    converted_text = converted_text.replace('черт; ', ' ####; ', 1)
# converted text
print(converted_text)
