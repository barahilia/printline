from printline.builder import chain


def test_simple():
    assert chain([
        [1],
        [2],
        [3],
    ]) == [
        [1, 2, 3]
    ]


def test_longer_sequences():
    assert chain([
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
    ]) == [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
