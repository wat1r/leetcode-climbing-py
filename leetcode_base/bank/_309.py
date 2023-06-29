from cmath import inf
from linecache import cache
from typing import List


class _1st:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @cache
        def dfs(i, hold):
            if i < 0:
                return -inf if hold else 0
            if hold:
                return max(dfs(i - 1, True), dfs(i - 2, False) - prices[i])
            else:
                return max(dfs(i - 1, False), dfs(i - 1, True) + prices[i])

        return dfs(n - 1, False)


class _2nd:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        f = [[0] * 2 for _ in range(n + 1)]  # [0]当前不持有股票，[1]当前持有股票
        f[0][0] = 0
        f[0][1] = -inf
        for i in range(1, n + 1):
            f[i][0] = max(f[i - 1][1] + prices[i - 1], f[i - 1][0])
            f[i][1] = max(f[i - 1][1], (f[i - 2][0] if i > 1 else 0) - prices[i - 1])
        return f[n][0]


class _3rd:
    print("")


class _4th:
    print("")

    if __name__ == '__main__':
        handlers = [_1st()]
        for handler in handlers:
            print("")
