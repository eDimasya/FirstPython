def switch_array_elements(switch_array, el_1: int, el_2: int):
    """
    перестановка двух элементов местами
    :param switch_array: Исходный массив
    :param el_1: индекс первого элемента
    :param el_2: индекс второго элемента
    :return: массив с изменёнными элементами
    """
    switch_array[el_1], switch_array[el_2] = switch_array[el_2], switch_array[el_1]
    return switch_array


def sort_bubble(array, printed=False):
    """
    Сортировка пузырьком одномерного массива
    :param printed: Выводить ли результат работы?
    :param array: Исходный массив
    :return: отсортированный массив
    """
    if printed:
        print("Bubble unsorted ARRAY:", array)
    # Количество операций
    counter = 0
    # Количество перестановок
    switches_counter = 0
    # признак сортировки массива
    sorted = False
    for x in array:
        switched = False
        counter += 1
        if not sorted:
            for y in range(1, len(array)):
                counter += 1
                if array[y - 1] > array[y]:
                    array = switch_array_elements(array, y - 1, y)
                    switches_counter += 1
                    switched = True
        else:
            break
        if switched:
            switched = False
        else:
            sorted = True
    if printed:
        print("Bubble sort COUNTER: ", counter, " SWITCHES: ", switches_counter)
        print("Bubble sorted ARRAY: ", array)
    return array


def sort_insert(unsorted_array):
    """
    Сортировка вставками одномерного массива
    :param unsorted_array: Исходный массив
    :return: отсортированный массив
    """
    pass


def sort_selection(array):
    """
    Сортировка выбором одномерного массива
    :param array: Исходный массив
    :return: отсортированный массив
    """
    for x in range(len(array)):
        min_array_index = x
        min_array = array[x]
        for y in range(x + 1, len(array)):
            if array[y] < min_array:
                min_array = array[y]
                min_array_index = y
        if min_array_index != x:
            array = switch_array_elements(array, x, min_array_index)
    return array


def sort_check():
    """
    Тест проверки сортировок
    """
    # тестовый массив
    test_array = [4, 2, 5, 1, 3]
    # Массив проверки перестановки
    test_switch_array = [4, 3, 5, 1, 2]

    # Тест перестановки элементов массива
    print("Switches test", end=": ")
    print("OK" if switch_array_elements(test_array, 1, 4) == test_switch_array else "FAIL")

    def sort_test(sort_algorithm):
        """
        Тестирование сортировки
        :param sort_algorithm: Алгоритм сортировки
        :return: если тест для алгоритмс пройден, то True, иначе False
        """

        def test_case_check(array_1, array_2, case_number):
            print("Test case #", case_number, end=": ")
            print("OK" if array_1 == array_2 else "FAIL")

        print("Тестируется сортировка:", sort_algorithm.__doc__)

        array_unsorted = [4, 2, 5, 1, 3]
        array_sorted = [1, 2, 3, 4, 5]
        sort_algorithm(array_unsorted)
        test_case_check(array_unsorted, array_sorted, 1)

        array_unsorted = list(range(10, 20)) + list(range(10))
        array_sorted = list(range(20))
        sort_algorithm(array_unsorted)
        test_case_check(array_unsorted, array_sorted, 2)

        array_unsorted = [4, 2, 4, 2, 3]
        array_sorted = [2, 2, 3, 4, 4]
        sort_algorithm(array_unsorted)
        test_case_check(array_unsorted, array_sorted, 3)

    # Тест сортировки выбором
    sort_test(sort_selection)

    # Тест сортировки пузырьком
    sort_test(sort_bubble)

    # Тест сортировки вставками
    sort_test(sort_insert)


sort_check()


