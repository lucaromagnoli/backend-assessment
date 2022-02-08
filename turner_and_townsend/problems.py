from typing import Optional, List


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

    def __str__(self):
        return self.value

    @classmethod
    def _validate_string(cls, string_value):
        for c in string_value:
            if c not in cls.numbers_map:
                raise ValueError('Not a valid Roman number')
        return string_value

    def to_integer(self):
        return sum(self.numbers_map[c] for c in self.value)


def roman_to_integer(string: str) -> int:
    """Convert a Roman number string to integer"""
    roman = RomanNumber(string)
    return roman.to_integer()


class Stack:
    """Stack implementation using list"""
    def __init__(self, stack: Optional[List] = None):
        if stack is None:
            self.stack = []
        else:
            self.stack = stack

    def __str__(self):
        return f'{self.stack}'

    def __eq__(self, other):
        return self.stack == other

    def add(self):
        self.check_stack_for_operation('+')
        first = self.pop()
        second = self.pop()
        self.push(first + second)

    def sub(self):
        self.check_stack_for_operation('-')
        first = self.pop()
        second = self.pop()
        self.push(first - second)

    def mul(self):
        self.check_stack_for_operation('*')
        first = self.pop()
        second = self.pop()
        self.push(first * second)

    def div(self):
        self.check_stack_for_operation('/')
        first = self.pop()
        second = self.pop()
        value = int(first/second)
        self.push(value)

    def check_stack_for_operation(self, operation):
        if len(self.stack) < 2:
            raise ValueError(f'Cannot apply {operation} operation to a stack with less than two elements')

    def pop(self):
        return self.stack.pop()

    def push(self, n):
        return self.stack.append(n)

    def swap(self):
        first = self.pop()
        second = self.pop()
        self.push(first)
        self.push(second)

    def dup(self):
        self.push(self.stack[-1])


class FifthError(ValueError):
    pass


class FifthInterpreter:
    ops_map = {
        '+': 'add',
        '-': 'sub',
        '*': 'mul',
        '/': 'div',
        'POP': 'pop',
        'SWAP': 'swap',
        'DUP': 'dup'
    }

    def __init__(self):
        self.stack = Stack()

    def _unknown_operation_exception(self, command):
        """Raise value error if command is unknown"""
        raise ValueError(f'Unknown operation: {command}')

    def parse_input_line(self, string_input):
        if string_input.startswith('PUSH'):
            self._parse_push_line(string_input)
        else:
            self._execute_operation(string_input)

    def _parse_push_line(self, string_input):
        operation, value = string_input.split()
        if operation != 'PUSH':
            self._unknown_operation_exception(operation)
        try:
            value = int(value)
        except ValueError as e:
            raise FifthError(str(e))
        self.stack.push(value)

    def _execute_operation(self, string_input):
        if string_input in self.ops_map:
            op_str = self.ops_map[string_input]
            op = getattr(self.stack, op_str)
            try:
                op()
            except (IndexError, ValueError) as e:
                raise FifthError(str(e))
        else:
            self._unknown_operation_exception(string_input)
