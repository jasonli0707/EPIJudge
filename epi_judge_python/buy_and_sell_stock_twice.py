from typing import List

from test_framework import generic_test


def brute_force(prices):
    '''O(n^4) Time, O(1) Space'''
    n = len(prices)
    max_profit = 0.0
    for i in range(n):
        for j in range(i, n):
            for k in range(j, n):
                for l in range(k, n):
                    first = prices[j]-prices[i]
                    second = prices[l]-prices[k]
                    max_profit = max(max_profit, first + second)

    return max_profit


def n_square_sol(A):
    '''O(n^2) Time, O(1) Space'''
    def buy_and_sell_stock_once(prices):
        max_profit, min_price = 0.0, float('inf')
        for p in prices:
            diff = p - min_price
            max_profit = max(max_profit, diff)
            min_price = min(min_price, p)
        return max_profit 
   
    n = len(A) 
    max_profit = 0.0
    for i in range(n):
        first = buy_and_sell_stock_once(A[:i])
        second = buy_and_sell_stock_once(A[i:])
        max_profit = max(max_profit, first+second)
    return max_profit


def buy_and_sell_stock_twice(prices: List[float]) -> float:
    """find max profit buying and selling a share at most twice
       Time: O(n) 
       Space: O(n)

    Args:
        prices (List[float]): a sequences of stock prices for n consecutive days

    Returns:
        float: max profit
    """
    n = len(prices) 
    max_profit_forward = [0]*n # i-th element stores the max profit from 0 to i-th day

    # compute max profit from 0 to i
    max_total_profit = 0.0
    min_value = float('inf')
    # for i in range(n):
    for i, p in enumerate(prices):
        min_value = min(min_value, p)
        max_total_profit = max(max_total_profit, p - min_value)
        max_profit_forward[i] = max_total_profit

    # compute max profit from n-2 to 1
    backward_profit = 0.0
    max_value = float('-inf')

    # for i in reversed(range(1, n)):
    for i, p in reversed(list(enumerate(prices[1:], 1))):
        max_value = max(max_value, p)
        backward_profit = max(backward_profit, max_value - p)
        max_total_profit = max(max_total_profit, backward_profit+max_profit_forward[i-1]) # max profit from 0 to i-1 + max profit from i to n-1

    return max_total_profit
    

    


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
