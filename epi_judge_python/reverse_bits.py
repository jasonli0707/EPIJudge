from test_framework import generic_test


def brute_force(x, SIZE=16):
    '''
    Time Complexity: O(n)
    Space Complexity: O(n)
    1) take the lowest bit at a time
    2) perform a left shift operation to its reverse ordered position
    3) OR with output y
    '''
    y = 0
    position = SIZE -1
    while x:
        y |= (x & 1) << position
        position -= 1
        x = x >> 1
    return y


PRECOMPUTED_REVERSE = [] # array-based lookup-table
def build_cache():
    '''
    Pre-compute lookup table for 16-bit integers
    '''
    print('building lookup table...')
    for i in range(0, 2**16):
        PRECOMPUTED_REVERSE.append(brute_force(i))
    print('Done')

def reverse_bits(x: int) -> int:
    """reverse all the bits in an unsigned integer using table lookup
       Time Complexity: O(n/L)
       Space Complexity: O(2^L)
    Args:
        x (int): 64-bit unsigned integer

    Returns:
        int: 64-bit unsigned integer with bits of the input in reverse order
    """

    MASK_SIZE= 16
    BIT_MASK = 0xFFFF
    
    return (PRECOMPUTED_REVERSE[x & BIT_MASK] << (3*MASK_SIZE) \
            | PRECOMPUTED_REVERSE[(x>>MASK_SIZE) & BIT_MASK] << (2*MASK_SIZE) \
            | PRECOMPUTED_REVERSE[(x>>(2*MASK_SIZE)) & BIT_MASK] << MASK_SIZE \
            | PRECOMPUTED_REVERSE[(x>>(3*MASK_SIZE)) & BIT_MASK])




if __name__ == '__main__':
    build_cache()
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
