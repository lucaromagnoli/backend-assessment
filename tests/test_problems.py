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
