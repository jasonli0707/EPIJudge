from test_framework import generic_test


def power(x: float, y: int) -> float:
    """Compute x^y 
       Time Complexity: O(logy) or O(n) where n is the number of bits in y
       i.e. (x^y) ==> (x^2)^(y/2) ==> (x^4)^(y/4) ==> (x^8)^(y/8) ==> (x^16)^(y/16) ...
       https://www.geeksforgeeks.org/write-an-iterative-olog-y-function-for-powx-y/
    Args:
        x (float): floating point number
        y (int): an integer

    Returns:
        float: x^y
    """
    result = 1.0
    power = y
    if y<0:
        power, x = -power, 1.0/x
    while power:
        if power & 1: # if y is odd
            result *= x # x^y = x*(x^2)^(y/2)
        x, power = x*x, power >> 1 # x = x^2, y = y/2
    return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
