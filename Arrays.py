"""
A = [1, 2, 3, 4, 5]
for x in A:
    print(x, type(x))
    x += 1
    print(x)
print(A)

for k in range(5):
    A[k] *= A[k]
print(A)

A = [0] * 10
top = 0
x = int(input())
while x != 0:
    A[top] = x
    top += 1
    x = int(input())

for k in range(top - 1, -1, -1):
    print(A[k])
print(A)
"""
"""
N = int(input())
A = [0] * N
B = [0] * N
for k in range(N):
    A[k] = int(input())
for k in range(N):
    B[k] = A[k]
C = list(A)
print(C)
"""


def array_search(A:list, N:int, x:int):
    """
    Посик числа x в массиве A от 0 до N-1 включительно
    :param A: Массив
    :param N:
    :param x:
    :return: индекс элемента x в массиве A, или -1, если нет элемента
    Если несколько одинаковых, равных x, то вернуть индекс первого
    """
    for k in range(N):
        if A[k] == x:
            return k
    return -1


def test_array_search():
    A1 = [1, 2, 3, 4, 5]
    m = array_search(A1, 5, 8)
    if m == -1:
        print("test1 OK")
    else:
        print("test1 fail")

    A2 = [-1, -2, -3, -4, -5]
    m = array_search(A2, 5, -3)
    if m == -1:
        print("test2 OK")
    else:
        print("test2 fail")

    A3 = [10, -2, 10, 30, -5]
    m = array_search(A3, 5, 10)
    if m == -1:
        print("test2 OK")
    else:
        print("test2 fail")

test_array_search()