import pytest

from turner_and_townsend import problems


@pytest.fixture
def stack_with_data():
    return problems.Stack([1, 2])


@pytest.fixture
def interpreter():
    return problems.FifthInterpreter()


@pytest.fixture
def interpreter_with_data(interpreter):
    interpreter.parse_input_line('PUSH 1')
    interpreter.parse_input_line('PUSH 2')
    return interpreter


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


def test_stack_add(stack_with_data):
    stack_with_data.add()
    assert stack_with_data == [3]


def test_stack_sub(stack_with_data):
    stack_with_data.sub()
    assert stack_with_data == [1]


def test_stack_mul(stack_with_data):
    stack_with_data.mul()
    assert stack_with_data == [2]


def test_stack_div(stack_with_data):
    stack_with_data.div()
    assert stack_with_data == [2]


def test_stack_pop(stack_with_data):
    stack_with_data.pop()
    assert stack_with_data == [1]


def test_stack_push(stack_with_data):
    stack_with_data.push(3)
    assert stack_with_data == [1, 2, 3]


def test_stack_swap(stack_with_data):
    stack_with_data.swap()
    assert stack_with_data == [2, 1]


def test_stack_dup(stack_with_data):
    stack_with_data.dup()
    assert stack_with_data == [1, 2, 2]


def test_stack_arithmetic_exception():
    stack = problems.Stack()
    with pytest.raises(ValueError):
        stack.add()


def test_fifth_interpreter_push(interpreter):
    interpreter.parse_input_line('PUSH 1')
    assert interpreter.stack == [1]
    interpreter.parse_input_line('PUSH 2')
    assert interpreter.stack == [1, 2]


def test_fifth_interpreter_add(interpreter_with_data):
    interpreter_with_data.parse_input_line('+')
    assert interpreter_with_data.stack == [3]


def test_fifth_interpreter_sub(interpreter_with_data):
    interpreter_with_data.parse_input_line('-')
    assert interpreter_with_data.stack == [1]


def test_fifth_interpreter_mul(interpreter_with_data):
    interpreter_with_data.parse_input_line('*')
    assert interpreter_with_data.stack == [2]


def test_fifth_interpreter_div(interpreter_with_data):
    interpreter_with_data.parse_input_line('/')
    assert interpreter_with_data.stack == [2]


def test_fifth_interpreter_pop(interpreter_with_data):
    interpreter_with_data.parse_input_line('POP')
    assert interpreter_with_data.stack == [1]


def test_fifth_interpreter_swap(interpreter_with_data):
    interpreter_with_data.parse_input_line('SWAP')
    assert interpreter_with_data.stack == [2, 1]


def test_fifth_interpreter_dup(interpreter_with_data):
    interpreter_with_data.parse_input_line('DUP')
    assert interpreter_with_data.stack == [1, 2, 2]


def test_fifth_interpreter_exceptions_pop(interpreter):
    with pytest.raises(problems.FifthError):
        interpreter.parse_input_line('POP')


def test_fifth_interpreter_exceptions_push(interpreter):
    with pytest.raises(problems.FifthError):
        interpreter.parse_input_line('PUSH hello')


def test_fifth_interpreter_exceptions_swap(interpreter):
    with pytest.raises(problems.FifthError):
        interpreter.parse_input_line('DUP')


def test_fifth_interpreter_exceptions_dup(interpreter):
    interpreter.stack.push(1)
    with pytest.raises(problems.FifthError):
        interpreter.parse_input_line('SWAP')


def test_fifth_interpreter_exceptions_add(interpreter):
    interpreter.stack.push(1)
    with pytest.raises(problems.FifthError):
        interpreter.parse_input_line('+')


def test_fifth_interpreter_exceptions_sub(interpreter):
    interpreter.stack.push(1)
    with pytest.raises(problems.FifthError):
        interpreter.parse_input_line('-')


def test_fifth_interpreter_exceptions_mul(interpreter):
    interpreter.stack.push(1)
    with pytest.raises(problems.FifthError):
        interpreter.parse_input_line('*')


def test_fifth_interpreter_exceptions_div(interpreter):
    interpreter.stack.push(1)
    with pytest.raises(problems.FifthError):
        interpreter.parse_input_line('/')
