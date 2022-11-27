def comp_nearby_tuples(gap=2):
    def func(a, b):
        if a == b:
            return 0

        (a0, a1), (b0, b1) = a, b
        a_len, b_len = (a1 - a0), (b1 - b0)

        if abs(a_len - b_len) <= gap and abs(a0 - b0) <= gap:
            return 0

        if a0 == b0:
            assert a1 != b1
            a0, b0 = a1, b1

        if a0 < b0:
            return -1
        else:
            return 1

    return func


def comp_exact(a, b):
    if a == b:
        return 0
    elif a < b:
        return -1
    else:
        return 1


def _accords(arr, comp, same_ratio):
    indexes = [0] * len(arr)
    values = sorted(set(sum(arr, start=[])))

    for scan_value in values:
        same = 0

        for row in range(len(arr)):
            while indexes[row] < len(arr[row]):
                value = arr[row][indexes[row]]

                res = comp(value, scan_value)

                if res <= 0:
                    indexes[row] += 1

                if res == 0:
                    same += 1

                if res >= 0:
                    break

        if same >= same_ratio * len(arr):
            yield scan_value


def accords(arr, comp=None, same_ratio=1.):
    if comp is None:
        comp = comp_exact

    return list(_accords(arr, comp, same_ratio))
