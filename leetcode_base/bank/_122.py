from cmath import inf
from functools import cache
from typing import List


class _1st:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @cache
        def dfs(i, hold):
            if i < 0:
                return -inf if hold else 0
            if hold:
                return max(dfs(i - 1, True), dfs(i - 1, False) - prices[i])
            return max(dfs(i - 1, False), dfs(i - 1, True) + prices[i])

        return dfs(n - 1, False)


class _2nd:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        f = [[0] * 2 for _ in range(n + 1)]
        f[0][0] = 0
        f[0][1] = -inf
        for i in range(n):
            f[i + 1][0] = max(f[i][0], f[i][1] + prices[i])
            f[i + 1][1] = max(f[i][1], f[i][0] - prices[i])
        return f[n][0]


class _3rd:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        f0 = 0
        f1 = -inf
        for p in prices:
            new_f0 = max(f0, f1 + p)
            f1 = max(f1, f0 - p)
            f0 = new_f0
        return f0


class _4th:
    print("")


if __name__ == '__main__':
    handlers = [_1st()]
    for handler in handlers:
        print("")
