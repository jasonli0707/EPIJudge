from typing import List

from test_framework import generic_test

from math import isqrt # integer sqrt

def brute_force(n):
    '''Iterate i thru. 2 to n and check if every i is prime or not
       Time: O(n*n^1/2) = O(n^3/2)
       Space: O(k) number of primes 
    '''
    def is_prime(n):
        '''Time: O(sqrt(n)/2)'''
        if n == 2:
            return True
        elif n%2==0:
            return False

        for i in range(3, isqrt(n)+1, 2): # elimating all even i (if n is even, must be factorized by 2) => optimized trial division algorithm: https://www.geeksforgeeks.org/trial-division-algorithm-for-prime-factorization/
            if n%i==0: # if divisble by numbers other than 1 and itself
                return False 
        return True

    result = []
    for i in range(2, n+1):
       if is_prime(i):
           result.append(i) 
    return result

# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    '''
    sieve of eratosthenes algorithm
    Time: O(n*log(log(n)))
    Space: O(n)
    '''
    if n<2:
        return []

    result = []
    is_prime =[False, False] + [True]*(n-1) # binary array storing all states i.e. 0 and 1 are not primes
    for p in range(2, n+1):
        if is_prime[p]:
            result.append(p)
            for i in range(p*p, n+1, p):
                is_prime[i] = False # sieve all multiplies of p

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
