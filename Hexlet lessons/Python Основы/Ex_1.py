# BEGIN (write your solution here)
def binary(number):
    if not number:
        return '0'
    binary_number = ''
    remainder = number
    while remainder:
        bit = remainder % 2
        binary_number = str(bit) + binary_number
        remainder = remainder // 2
    return binary_number


print(binary(25))  # '1'
