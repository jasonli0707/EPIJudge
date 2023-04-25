from test_framework import generic_test


def evaluate(expression: str) -> int:
    s = []
    operators = {
        "+": lambda x, y: x+y,
        "-": lambda x, y: x-y,
        "*": lambda x, y: x*y,
        "/": lambda x, y: int(x/y),
    }

    for c in expression.split(","):
        if c in operators:
            y, x = s.pop(), s.pop()
            s.append(operators[c](x, y))
        else:
            s.append(int(c)) # add integer to the stack

    return s[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
