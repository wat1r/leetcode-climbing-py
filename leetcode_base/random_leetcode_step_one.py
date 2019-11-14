from typing import List


class RandomLeetcodeStepOne():

    def init(self):
        return ""

    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        def dp(i, j):
            if i == -1: return j + 1
            if j == -1: return i + 1

            if word1[i] == word2[j]:
                return dp(i - 1, j - 1)
            else:
                return min(dp(i, j - 1), dp(i - 1, j), dp(i - 1, j - 1)) + 1

        return dp(len(word1) - 1, len(word2) - 1)

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        return 1

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0 for _ in range(amount + 1)]
        for i in range(1, amount + 1):
            cost = float('inf')
            for c in coins:
                if i - c >= 0:
                    cost = min(cost, dp[i - c] + 1)
            dp[i] =cost
        if dp[amount] ==float('inf'):
            return -1
        else:
            return dp[amount]


    def test(self):
        amount = 10
        dp = [float("inf")] * (amount + 1)
        m = 3
        n = 4
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        return


if __name__ == '__main__':
    handler = RandomLeetcodeStepOne()
    # handler.init()
    # handler.minDistance()
    handler.test()
    handler.coinChange([1, 2, 5], 11)
