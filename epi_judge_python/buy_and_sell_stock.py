from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    '''
    return max profit for buying and selling a stock once
    Time: O(n)
    Space: O(1)
    '''
    if len(prices) < 2:
        return 0.0

    profit = 0.0 
    min_idx = 0

    for i in range(1, len(prices)):
        diff = prices[i] - prices[min_idx]
        profit = max(diff, profit)
        if prices[i] < prices[min_idx]:
            min_idx = i

    return profit 


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
