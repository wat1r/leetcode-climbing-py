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

        return 0

    def test(self):
        amount =10
        dp = [float("inf")] * (amount + 1)


        return


if __name__ == '__main__':
    handler = RandomLeetcodeStepOne()
    # handler.init()
    # handler.minDistance()
    handler.test()
