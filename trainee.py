test_list = ['Sansa Stark', -1, 3]


def is_arguments_for_substr_correct(input_string, start_index, length):
    if length < 0:
        return False
    elif start_index < 0:
        return False
    elif start_index > len(input_string)-1:
        return False


    else:
        return True


print(is_arguments_for_substr_correct(test_list))
