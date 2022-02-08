import click

from turner_and_townsend import problems


@click.group()
def cli():
    """Turner and Townsend backend assessment"""


def validate_collatz_input(ctx, param, value):
    try:
        return int(value)
    except ValueError:
        raise ValueError('Please provide a numerical value')


def validate_roman_input(ctx, param, value):
    return problems.RomanNumber(value)


@cli.command()
@click.argument('n', callback=validate_collatz_input)
def collatz(n: int):
    """Given a numeric input, count how many steps it takes until the Collatz sequence reaches 1."""
    steps = problems.collatz_conjecture(n)
    print(f'n: {n} | steps: {steps}')


@cli.command()
@click.argument('n', callback=validate_roman_input)
def roman(n: problems.RomanNumber):
    """Given a Roman number as a string, get its values as integer."""
    print(f'Roman: {n} | Integer: {n.to_integer()}')


@cli.command()
def fifth():
    """Run a Fifth interpreter and provide commands via keyboard input"""
    new_command = True
    interpreter = problems.FifthInterpreter()
    while new_command:
        string_input = input('Please enter a FIFTH command: ')
        try:
            interpreter.parse_input_line(string_input)
        except problems.FifthError as e:
            print(f'ERROR: {str(e)}')
        else:
            print(f'Stack is {interpreter.stack}')
        finally:
            new_command = input('Press Y to enter another command, N to quit: ').lower() == 'y'


if __name__ == '__main__':
    cli()
