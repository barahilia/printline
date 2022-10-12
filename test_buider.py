from builder import build, pairs, triplets


def xtest_trivial():
    assert build([
        [1, 1, 1]
    ]) == [[1, 1, 1]]


def xtest_single_column():
    assert build([
        [1],
        [2],
        [3],
    ]) == [[1], [2], [3]]


def xtest_simple_gap():
    assert build([
        [1, 1],
        [3, 2],
        [4, 3],
    ]) == [
        [1, 1],
        [3, 3],
    ]


def test_trivial_pairs():
    assert pairs([
        [1, 1],
        [2, 2],
        [4, 4],
    ]) == [1, 2, 4]


def test_with_gap():
    assert pairs([
        [1, 1],
        [2, 3],
        [3, 4],
    ]) == [1, 3]

    assert pairs([
        [1, 0],
        [2, 3],
        [3, 4],
    ]) == [3]

    assert pairs([
        [1, 1],
        [3, 2],
        [4, 3],
    ]) == [1, 3]


def xtest_different_height():
    assert pairs([
        [1]
    ]) == []


def test_trivial_triplets():
    assert triplets([
        [1, 2, 3, 4],
        [1, 2, 3, 4],
        [1, 2, 3, 4],
    ]) == [1, 2, 3, 4]


def test_triplet_with_gaps():
    assert triplets([
        [1, 3, 5, 7],
        [0, 1, 2, 3, 4, 5],
        [1, 2, 3, 5, 7, 8],
    ]) == [1, 3, 5]
