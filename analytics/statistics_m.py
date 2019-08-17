def mean(values):

    if values:
        m = sum(values) / len(values)
        return m
    return 0


def median(values):
    v = sorted(values)

    assert values

    if len(v) % 2 == 0:
        right = int(len(v) / 2)
        left = right - 1
        return (v[left] + v[right]) / 2

    if len(v) % 2 != 0:
        mid_point = len(v) // 2
        return (float(v[mid_point]))
