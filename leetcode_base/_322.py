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
    def coinChange2nd(self, coins: List[int], amount: int) -> int:
        return 0

if __name__ == '__main__':
    print("hello pack")
