from test_framework import generic_test


def add(x, y):
    '''Ripple Carry Adder
       Time Complexity: O(n)'''

    k = 1
    temp_x, temp_y = x, y
    running_sum = 0
    cin = 0
    while temp_x or temp_y: # check if all bits are processed
        xk, yk = (x&k), (y&k)
        cout = (xk&yk) | (xk&cin) | (yk&cin) # at least 2 out 3 "1" appears at position k
        running_sum |= (xk^yk^cin)
        cin, k = (cout<<1), (k<<1)
        temp_x, temp_y = (temp_x>>1), (temp_y>>1)
    
    return running_sum | cin

    

def multiply(x: int, y: int) -> int:
    """multiply two nonnegative integers using only low-level primitives i.e. bitwise shift-and-add
       Time Complexity: O(n^2)
    Args:
        x (int): 64-bit nonnegative integer
        y (int): 64-bit nonnegative integer

    Returns:
        int: the multiple of x and y
    """

    running_sum = 0
    while x:
        if (x&1): # if 1 appear at position k
            running_sum = add(running_sum, y)
        
        x, y = (x>>1), (y<<1) # y = y*2

    return running_sum


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_multiply.py',
                                       'primitive_multiply.tsv', multiply))
