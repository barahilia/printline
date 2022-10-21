from printline.builder import build, pairs, triplets, accords, \
    comp_nearby_tuples


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


def test_accords():
    assert accords([
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3],
    ]) == [
        1, 2, 3
    ]

    assert accords([
        [1, 2, 3],
        [2, 3],
        [2, 3],
    ]) == [
        2, 3
    ]

    assert accords([
        [2, 3],
        [1, 2, 3],
        [1, 2, 3],
    ]) == [
        2, 3
    ]


def test_tuple_accords():
    assert accords([
        [(1, 2), (3, 4)],
        [(3, 4)],
    ]) == [
        (3, 4)
    ]


def test_comp():
    checks = [
        {'a': (1, 2), 'b': (1, 2), 'res': 0},
        {'a': (10, 20), 'b': (8, 19), 'res': 0},
        {'a': (10, 20), 'b': (9, 21), 'res': 0},
        {'a': (10, 20), 'b': (11, 19), 'res': 0},
        {'a': (10, 20), 'b': (11, 23), 'res': 0},

        {'a': (10, 20), 'b': (7, 19), 'res': 1},
        {'a': (10, 20), 'b': (8, 21), 'res': 1},
        {'a': (10, 20), 'b': (7, 17), 'res': 1},
        {'a': (10, 20), 'b': (10, 17), 'res': 1},

        {'a': (10, 20), 'b': (11, 18), 'res': -1},
        {'a': (10, 20), 'b': (10, 23), 'res': -1},
        {'a': (10, 20), 'b': (11, 24), 'res': -1},
    ]

    for check in checks:
        assert comp_nearby_tuples(check['a'], check['b']) == check['res']


def test_nearby_accords():
    assert accords([
        [(10, 20)],
        [(8, 19)],
    ], comp=comp_nearby_tuples) == [
        (10, 20)
    ]
