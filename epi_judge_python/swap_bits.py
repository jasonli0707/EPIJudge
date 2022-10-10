from test_framework import generic_test


def swap_bits(x: int, i: int, j: int) -> int:
    """Swap bits in the ith and jth positions and return the binary word inplace
    Args:
        x (int): a binary word
        i (int): ith position
        j (int): jth position

    Returns:
        int: return x inplace
    """

    # First extract the ith and jth bits and check if they are equal
    # if equal then no change
    # else flip the bits in ith and jth position using XOR i.e. 1^1 = 0 and 0^1 = 1
    # Time Complexity O(1)
    if ((x>>i) & 1) != ((x>>j) & 1) :
        bit_mask = (1 << i) | (1 << j)
        x ^= bit_mask

    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))
