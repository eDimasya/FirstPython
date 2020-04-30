def arrays_left_turn(A, N):
    """
    Циклический сдвиг влево
    :param A: искомый массив
    :param N: количество перменных
    :return: массив, сдвинутый влево
    """
    temp = A[0]
    for k in range(N - 1):
        A[k] = A[k + 1]
    A[N - 1] = temp
    return A


def test_array_left_turn():
    A1 = [1, 2, 3, 4, 5]
    A1 = arrays_left_turn(A1, 5)
    print(A1)
    if A1 == [2, 3, 4, 5, 1]:
        print("Test #1 OK")
    else:
        print("Test #1 Fail")


test_array_left_turn()
