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


if __name__ == '__main__':
    print("hello pack")
    handler = Solution()
    handler.change([1, 2, 5], 5)
