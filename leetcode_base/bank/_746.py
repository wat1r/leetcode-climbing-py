from typing import List


class _1st:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        f = [0] * (n + 1)
        f[0] = cost[0]
        f[1] = cost[1]
        for i in range(2, n + 1):
            f[i] = min(f[i - 1], f[i - 2]) + (cost[i] if i < n else 0)
        return f[n]


class _2nd:
    print("")


class _3rd:
    print("")


class _4th:
    print("")


if __name__ == '__main__':
    handlers = [_1st()]
    for handler in handlers:
        handler.minCostClimbingStairs([10, 15, 20])
