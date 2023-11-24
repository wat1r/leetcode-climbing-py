from math import inf
from typing import List


class _1st:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        f = [[inf] * n for _ in range(m)]
        f[-1] = grid[-1]
        for i in range(m - 2, -1, -1):
            for j, g in enumerate(grid[i]):
                for k, c in enumerate(moveCost[g]):  # 移动到下一行的第 k 列
                    f[i][j] = min(f[i][j], f[i + 1][k] + c)
                f[i][j] += g
        return min(f[0])


class _2nd:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m - 2, -1, -1):
            for j in range(n):
                grid[i][j] += min(g + c for g, c in zip(grid[i + 1], moveCost[grid[i][j]]))
        return min(grid[0])


class _3rd:
    print("")


class _4th:
    print("")


if __name__ == '__main__':
    handlers = [_1st()]
    for handler in handlers:
        grid = [[5, 3], [4, 0], [2, 1]]
        moveCost = [[9, 8], [1, 5], [10, 12], [18, 6], [2, 4], [14, 3]]
        handler.minPathCost(grid, moveCost)
