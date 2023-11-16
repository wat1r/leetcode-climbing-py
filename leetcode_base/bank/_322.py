from cmath import inf
from linecache import cache
from typing import List


class Solution:
    # 01背包
    def coinChange1st(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        # 初始化数组 dp[amount+1] 为 float('inf')
        dp = [float('inf') for i in range(amount + 1)]
        dp[0] = 0
        for i in range(1, n + 1):
            for j in range(amount, coins[i - 1], -1):
                dp[j] = min(dp[j], dp[j - coins[i]] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1

    # 完全背包
    def change(self, coins: List[int], amount: int) -> int:
        # 初始化数组 dp[amount+1] 为 float('inf')
        dp = [float('inf') for i in range(amount + 1)]
        dp[0] = 0
        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] = min(dp[j], dp[j - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1

    # 多重背包
    def change(self, coins: List[int], amount: int, t: List[int]) -> int:
        dp = [float('inf') for i in range(amount + 1)]
        dp[0] = 0
        for i in range(len(coins)):
            for j in range(amount, coins[i] - 1, -1):
                for k in range(1, t[i] + 1):
                    if j >= k * coins[i]:
                        dp[j] = min(dp[j], dp[j - k * coins[i]] + k)
        return -1 if dp[amount] > amount else dp[amount]


class _1st:
    # capacity:背包容量，w[i]:第i个物品的体积，v[i]:第i个物品的价值
    # 所选物品和的体积和不超过capacity的前提下，所能得到的最大价值和
    # 每种物品可以无限次重复选
    def unbounded_knapsack(capacity: int, w: List[int], v: List[int]) -> int:
        n = len(w)

        @cache
        def dfs(i, c):
            if i < 0:
                return 0
            if c < w[i]:
                return dfs(i - 1, c)
            return max(dfs(i - 1, c), dfs(i, c - w[i]) + v[i])

        return dfs(n - 1, capacity)

    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)

        @cache
        def dfs(i, c):
            if i < 0:
                return 0 if c == 0 else inf
            if c < coins[i]:
                return dfs(i - 1, c)
            return min(dfs(i - 1, c), dfs(i, c - coins[i]) + 1)

        ans = dfs(n - 1, amount)
        return ans if ans < inf else -1


class _2nd:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        f = [[inf] * (amount + 1) for _ in range(n + 1)]
        f[0][0] = 0
        for i, x in enumerate(coins):
            for c in range(amount + 1):
                if c < x:
                    f[i + 1][c] = f[i][c]
                else:
                    f[i + 1][c] = min(f[i][c], f[i + 1][c - x] + 1)
        ans = f[n][amount]
        return ans if ans < inf else -1


class _3rd:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        f = [inf] * (amount + 1)
        f[0] = 0
        for i, x in enumerate(coins):
            for c in range(x, amount + 1):
                    f[c] = min(f[c], f[c - x] + 1)
        ans = f[amount]
        return ans if ans < inf else -1


if __name__ == '__main__':
    print("hello pack")
    handler = Solution()
    handler.change([1, 2, 5], 5)
