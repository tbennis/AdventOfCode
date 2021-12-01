def reverse_number(number):
    reverse = 0
    while number > 0:
        remainder = number % 10
        reverse = reverse * 10 + remainder
        number = (number - remainder) / 10
    return int(reverse)
    