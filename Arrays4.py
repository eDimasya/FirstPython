"""Решето Эратосфена"""

def eratosphen(N):
    """
    Вывод простых числе от 0 до N
    :param N: количсетво элементов
    :return: массив, с простыми числами
    """
    temp_array = [True] * N
    temp_array[0] = temp_array[1] = False
    for k in range(2, N):
        if temp_array[k]:
            for m in range(2 * k, N, k):
                temp_array[m] = False
    counter_array = 0
    for k in range(N):
        if temp_array[k]:
            counter_array += 1
    index_result = 0
    result = [0] * counter_array
    for k in range(N):
        if temp_array[k]:
            result[index_result] = k
            index_result += 1
    print(result)
    return result


def test_eratosphen():
    N = 30
    A = eratosphen(N)
    print(A)
    if A == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
        print("Test #1 OK")
    else:
        print("Test #2 Fail")


test_eratosphen()
