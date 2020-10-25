def error_processing(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            f = open('text.txt', 'a+')
            f.write(f'{str(e)} \n')
            f.close()

    return wrapper


@error_processing
def function(name_file: str):
    n = 42/0
    dataset_file = open(f"{name_file}.txt", encoding='utf-8')


name = 'text'
function(name)
