import time

PALINDROME: str = 'deified'
NOT_PALINDROME: str = 'deiabgied'
counting_occurrences_and_results: dict = {}
entry_counter: int = 0


def executing_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func_name = str(func)
        result = func(*args, **kwargs)
        end = time.time()
        duration_of_execution = end - start
        print(f'[*] Время выполнения: {duration_of_execution} секунд.')
        if func_name in counting_occurrences_and_results:  # if it is two or more calls to this func
            middle_result_list = counting_occurrences_and_results.get(func_name)  # extracting values from dict
            middle_result_list[0] += 1  # incrementing number of calls
            middle_result_list.append(duration_of_execution)  # adding new execution time
            # average execution time
            functions_average_time_processing = sum(middle_result_list[1:]) / middle_result_list[0]
            print(f'[*] Среднее время выполнения данной функции: {functions_average_time_processing} секунд.')
        else:  # first adding into dict
            counting_occurrences_and_results[func_name] = [1, duration_of_execution]
        return result

    return wrapper


@executing_time
def palindrome_check(user_input: str) -> bool:
    temp = list(user_input)
    time.sleep(0.4)
    while len(temp) >= 0:
        if len(temp) == 0 or len(temp) == 1:
            return True
        if temp[0] == temp[-1]:
            temp = temp[1:-1]
        else:
            return False


temp1 = palindrome_check(PALINDROME)
temp2 = palindrome_check(NOT_PALINDROME)
temp3 = palindrome_check('aba')
temp4 = palindrome_check('12344321')
print(temp1)
print(temp2)
print(temp3)
print(temp4)
