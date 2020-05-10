def check_array(array):
    """
    Функция проверки массива на правильность
    :param array: Исходный массив
    :return: True, если с массивом всё в порядке. False, если массив ошибочный
    """
    if array is None:
        return False
    if not array:
        return False
    if type(array) != list:
        return False
    if type(array) == list:
        if len(array) >= 1:
            return True
        else:
            return False
    return False


def sort_bubble(array, printed=False):
    """
    Сортировка пузырьком одномерного массива
    :param printed: Выводить ли результат работы?
    :param array: Исходный массив
    :return: отсортированный массив
    """
    if check_array(array):
        if printed:
            print("Bubble unsorted ARRAY:", array)
        # Количество операций
        counter = 0
        # Количество перестановок
        switches_counter = 0
        for bypass in range(len(array)):
            counter += 1
            for y in range(1, len(array) - bypass):
                counter += 1
                if array[y - 1] > array[y]:
                    array[y - 1], array[y] = array[y], array[y - 1]
                    switches_counter += 1
        if printed:
            print("Bubble sort COUNTER: ", counter, " SWITCHES: ", switches_counter)
            print("Bubble sorted ARRAY: ", array)
        return array
    else:
        print("Arguments Error! it's Not ARRAY!!")


def sort_insert(array, printed=False):
    """
    Сортировка вставками одномерного массива
    :param printed: Нужно ли печатать результаты?
    :param array: Исходный массив
    :return: отсортированный массив
    """
    if check_array(array):
        if printed:
            print("Insert sort ARRAY: ", array)
        # Количество операций
        counter = 0
        # Количество перестановок
        switches_counter = 0
        for top in range(1, len(array)):
            k = top
            while k > 0 and array[k] < array[k - 1]:
                array[k], array[k - 1] = array[k - 1], array[k]
                k -= 1
                counter += 1
                switches_counter += 1
        if printed:
            print("Insert sort COUNTER: ", counter, " SWITCHES: ", switches_counter)
            print("Insert sorted ARRAY: ", array)
        return array
    else:
        print("Arguments Error! it's Not ARRAY!!")


def sort_selection(array, printed=False):
    """
    Сортировка выбором одномерного массива
    :param printed: Нужно ли выводить результат?
    :param array: Исходный массив
    :return: отсортированный массив
    """
    if check_array(array):
        if printed:
            print("Selection unsorted ARRAY: ", array)
        # Количество операций
        counter = 0
        # Количество перестановок
        switches_counter = 0
        for pos in range(len(array) - 1):
            min_array_index = pos
            min_array = array[pos]
            for k in range(pos + 1, len(array)):
                counter += 1
                if array[k] < min_array:
                    min_array = array[k]
                    min_array_index = k
            if min_array_index != pos:
                array[pos], array[min_array_index] = array[min_array_index], array[pos]
                switches_counter += 1
        if printed:
            print("Selection sort COUNTER: ", counter, " SWITCHES: ", switches_counter)
            print("Selection sorted ARRAY: ", array)
        return array
    else:
        print("Arguments Error! it's Not ARRAY!!")


def sort_check():
    """
    Тест проверки сортировок
    """
    # Тест функции проверки массива
    def test_case_check_array(array, case_number):
        """
        Функция проверки тест кейсов проверки массива
        :param array: Исходный массив
        :param case_number: Номер кейса
        :return: True, Если проверка пройдена, иначе False
        """
        print("Check Array Test Case #", case_number, end=": ")
        print("OK" if check_array(array) else "FAIL")

    test_case_check_array([4, 2, 5, 1, 3], 1)
    test_case_check_array([], 2)
    test_case_check_array(None, 3)
    test_case_check_array(4, 4)
    test_case_check_array(False, 5)
    test_case_check_array("Test", 6)

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
        test_case_check(sort_algorithm(array_unsorted, True), array_sorted, 1)

        array_unsorted = list(range(10, 20)) + list(range(10))
        array_sorted = list(range(20))
        test_case_check(sort_algorithm(array_unsorted), array_sorted, 2)

        array_unsorted = [4, 2, 4, 2, 3]
        array_sorted = [2, 2, 3, 4, 4]
        test_case_check(sort_algorithm(array_unsorted), array_sorted, 3)

    # Тест сортировки выбором
    sort_test(sort_selection)
    # Тест сортировки пузырьком
    sort_test(sort_bubble)
    # Тест сортировки вставками
    sort_test(sort_insert)


sort_check()
