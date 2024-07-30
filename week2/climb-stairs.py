class Solution:
    def climbStairs(self, n: int) -> int:
        def climb(i, memo):
            if i < -1:
                return 0
            if i == -1:
                return 1
            if memo[i] == -1:
                memo[i] = climb(i-1, memo) + climb(i-2, memo)
            return memo[i]

        memo = [-1] * n
        return climb(n-1, memo)
        