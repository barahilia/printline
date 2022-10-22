def comp_nearby_tuples(a, b):
    if a == b:
        return 0

    (a0, a1), (b0, b1) = a, b
    a_len, b_len = (a1 - a0), (b1 - b0)

    if abs(a_len - b_len) <= 2 and abs(a0 - b0) <= 2:
        return 0

    if a0 == b0:
        assert a1 != b1
        a0, b0 = a1, b1

    if a0 < b0:
        return -1
    else:
        return 1


def comp_exact(a, b):
    if a == b:
        return 0
    elif a < b:
        return -1
    else:
        return 1


def _accords(arr, comp):
    main, others = arr[0], arr[1:]
    indexes = [0] * len(others)
    values = [None] * len(others)

    for main_value in main:
        for row in range(len(others)):
            while indexes[row] < len(others[row]):
                values[row] = others[row][indexes[row]]

                if comp(values[row], main_value) >= 0:
                    break

                indexes[row] += 1

        if {comp(main_value, value) for value in values} == {0}:
            yield main_value


def accords(arr, comp=None):
    if comp is None:
        comp = comp_exact

    return list(_accords(arr, comp))
