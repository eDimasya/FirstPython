def is_simple_number(x):
    """"Является ли число простым
        x - целое положительное число
        Если простое, то возвращает True,
        Иначе - False
    """
    divisor = 2
    while divisor < x:
        if x % divisor == 0:
            return False
        divisor += 1
    return True


def factorize_number(x):
    """
    Раскладывает число на множители
    :param x: целое положительное
    :return: Печатет на экран
    """
    divisor = 2
    while x > 1:
        if x % divisor == 0:
            print(divisor)
            x //= divisor
        else:
            divisor += 1

