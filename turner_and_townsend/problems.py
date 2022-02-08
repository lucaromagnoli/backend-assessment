def collatz_conjecture(n: int) -> int:
    """Given a numeric input, count how many steps it takes until the Collatz sequence reaches 1.

    The Collatz, or 3n + 1 conjecture, is a mathematical sequence defined as follows:
    * start with a number, n
    * if n is even:
      * produce n / 2
    * otherwise, n is odd:
      * produce 3 * n + 1
    * repeat until n is 1
    """
    def count_sequence(_n: int, steps: int = 0):
        if _n == 1:
            return steps
        elif _n % 2 == 0:
            return count_sequence(_n/2, steps=steps + 1)
        else:
            return count_sequence(3 * _n + 1, steps=steps + 1)
    if n < 1:
        raise ValueError('Please enter a positive integer')
    return count_sequence(n)


class RomanNumber:
    numbers_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'C': 100,
        'M': 1000
    }

    def __init__(self, value):
        self.value = self._validate_string(value)

    @classmethod
    def _validate_string(cls, string_value):
        for c in string_value:
            if c not in cls.numbers_map:
                raise ValueError('Not a valid Roman number')
        return string_value

    def to_integer(self):
        return sum(self.numbers_map[c] for c in self.value)


def roman_to_integer(string):
    """Convert a Roman number string to integer"""
    roman = RomanNumber(string)
    return roman.to_integer()
