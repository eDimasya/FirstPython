def invert_array(A, N):
    """
    Обращение масива задом наперёд
    :param A:
    :param N:
    :return: Обратный массив до N-1
    """
    B = [0] * N
    for k in range(N):
        B[k] = A[N - 1 - k]
    return B


def test_invert_array():
    a1 = [1, 2, 3, 4, 5]
    a1 = invert_array(a1, 5)
    print(a1)
    if a1 == [5, 4, 3, 2, 1]:
        print("Test #1 OK")
    else:
        print("Test #1 FAIL")

    a2 = [0, 0, 0, 0, 0, 10]
    a2 = invert_array(a2, 6)
    print(a2)
    if a2 == [10, 0, 0, 0, 0, 0]:
        print("Test #1 OK")
    else:
        print("Test #1 FAIL")


test_invert_array()
