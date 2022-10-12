def _build(arr):
    line = []

    for vindex in range(len(arr)):
        hindex = 0
        value = arr[vindex][hindex]

        for hindex in range(1, len(arr[vindex])):
            while arr[value]:
                pass

    for line in arr:
        yield line


def build(arr):
    return list(_build(arr))


def _pairs(arr):
    first_column_index = 0
    second_column_index = 0

    for first_column_index in range(len(arr)):
        first = arr[first_column_index][0]

        while second_column_index < len(arr):
            second = arr[second_column_index][1]

            if second >= first:
                break

            second_column_index += 1

        if first == second:
            yield first


def pairs(arr):
    return list(_pairs(arr))


def _triplets(arr):
    a, b, c = arr
    b_index = c_index = 0

    for a_value in a:
        while b_index < len(b):
            b_value = b[b_index]

            if b_value >= a_value:
                break

            b_index += 1

        while c_index < len(c):
            c_value = c[c_index]

            if c_value >= a_value:
                break

            c_index += 1

        if a_value == b_value == c_value:
            yield a_value


def triplets(arr):
    return list(_triplets(arr))


def _accords(arr):
    main, others = arr[0], arr[1:]
    indexes = [0] * len(others)
    values = [None] * len(others)

    for main_value in main:
        for row in range(len(others)):
            while indexes[row] < len(others[row]):
                values[row] = others[row][indexes[row]]

                if values[row] >= main_value:
                    break

                indexes[row] += 1

        if all(main_value == value for value in values):
            yield main_value


def accords(arr):
    return list(_accords(arr))
