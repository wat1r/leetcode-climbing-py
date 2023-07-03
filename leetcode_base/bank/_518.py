from typing import List


class _1st:
    #     public int change1st(int amount, int[] coins) {
    #         int n = coins.length;
    #         int[][] dp = new int[n + 1][amount + 1];
    #         dp[0][0] = 1;
    #         for (int i = 1; i <= n; i++) {
    #             for (int j = 0; j <= amount; j++) {
    #                 for (int k = 0; k * coins[i - 1] <= j; k++) {
    #                     dp[i][j] += dp[i - 1][j - k * coins[i - 1]];
    #                 }
    #             }
    #         }
    #         return dp[n][amount];
    #     }
    def change(self, t: int, coins: List[int]) -> int:
        n = len(coins)
        f = [[0] * (t + 1) for _ in range(n + 1)]
        f[0][0] = 1
        for i in range(1, n + 1):
            for j in range(0, t + 1):
                # for k in range(0, )
                for k in range(0, 5001):
                    if k * coins[i - 1] > j:
                        break
                    print(i, j, k)
                    f[i][j] += f[i - 1][j - k * coins[i - 1]]
        return f[n][t]


class _2nd:
    print("")


class _3rd:
    print("")


class _4th:
    print("")


if __name__ == '__main__':
    handlers = [_1st()]
    for handler in handlers:
        handler.change(5, [1, 2, 5])
