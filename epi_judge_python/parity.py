from cgitb import reset
from test_framework import generic_test

def brute_force(x):
    '''
    Time complexity: O(n) where n is the number of bits in x
    '''
    result = 0 # either 1 or 0
    while x:
        result ^= x & 1 # (result XOR (x AND 1)) => (result + (x AND 1)) mod 2
        x = x>> 1
        
    return result

def erase_lowest_set_bit(x):
    '''
    This method uses the fact that x & (x-1) can erase the lowest bit that is set to 1.
    Time complexity: O(k) where k is the number of bits that are set to 1 in x
    '''
    result = 0 # either 1 or 0
    while x:
        result ^= 1 # count 1 then mod 2
        x &= (x-1) # erase the lowest set bit in x
        
    return result

def xor_parity(x):
    '''
    This method uses the fact that XOR of a group of bits is its parity i.e. <b63,...,b32> XOR <b32, ..., b0> = parity(<b64,..b0>)
    Time complexity: O(logn) where n is the number of bits in x
    '''
    x ^= x>>32
    x ^= x>>16
    x ^= x>>8
    x ^= x>>4
    x ^= x>>2
    x ^= x>>1
    return x & 0x1 # mask out the last bit

def parity(x: int) -> int:
    """Computing the parity of a binary word. The parity of a binary word is 1 if the number of 1s is odd; otherwise it is 0. 
    Args:
        x (int): an integer

    Returns:
        int: the parity of the input
    """
    x ^= x>>32
    x ^= x>>16
    x ^= x>>8
    x ^= x>>4
    x ^= x>>2
    x ^= x>>1
        
    return x & 0x1 # mask out the last bit


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
