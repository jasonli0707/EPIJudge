from typing import List

from test_framework import generic_test, test_utils

MAPPING = ["0", "1", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]


def phone_mnemonic_loop(phone_number):
    result = ['']
    for digit in range(len(phone_number)):
        new_result = []
        for prev in result:
            for c in MAPPING[int(phone_number[digit])]:
                new_result.append(prev + c) # add one more charater to all strings from previous step 
            result = new_result # update the result to current step
    return result

def phone_mnemonic(phone_number: str) -> List[str]:
    '''
    Time: O(4^n*n) where 4^n is the complexity of recursion call T(n) <= 4T(n-1) i.e. at most 4 calls per step
    '''
    def phone_mnemonic_helper(digit):
        if digit == len(phone_number): # base case
            mnemonics.append(''.join(partial_mnenomic)) # arrive one particular solution & add result to list = O(n) time
        else:
            for c in MAPPING[int(phone_number[digit])]: # try all possible characters for this digit
                partial_mnenomic[digit] = c
                phone_mnemonic_helper(digit+1)

    mnemonics, partial_mnenomic = [], [0]* len(phone_number)
    phone_mnemonic_helper(0)
    return mnemonics


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic_loop,
            comparator=test_utils.unordered_compare))
