import pytest

from turner_and_townsend import problems

collatz_conjecture_test_data = [
    (1, 0),
    (2, 1),
    (9, 19),
    (100, 25)
]


@pytest.mark.parametrize('n, expected', collatz_conjecture_test_data)
def test_conjecture(n, expected):
    assert problems.collatz_conjecture(n) == expected


def test_conjecture_exception():
    with pytest.raises(ValueError):
        assert problems.collatz_conjecture(0)


def test_roman_number_class():
    assert problems.RomanNumber('XII')
    with pytest.raises(ValueError):
        problems.RomanNumber('SPQR')


roman_to_integer_test_data = [
    ('X', 10),
    ('VI', 6),
    ('MXVII', 1017),
]


@pytest.mark.parametrize('n, expected', roman_to_integer_test_data)
def test_roman_to_integer(n, expected):
    assert problems.roman_to_integer(n) == expected
