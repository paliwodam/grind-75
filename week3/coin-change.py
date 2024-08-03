# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin.

from math import inf
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = [inf] * (amount + 1)
        memo[0] = 0

        for coin in coins:
            for amt in range(coin, amount + 1):
                memo[amt] = min(memo[amt], memo[amt-coin] + 1)

        return memo[amount] if memo[amount] != inf else -1
