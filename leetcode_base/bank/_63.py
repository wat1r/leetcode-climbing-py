from typing import List


class _1st:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if grid[0][0] == 1:
            return 0
        f = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    continue
                if i == 0 and j == 0:
                    f[i][j] = 1
                elif i == 0:
                    f[i][j] = f[0][j - 1]
                elif j == 0:
                    f[i][j] = f[i - 1][0]
                else:
                    f[i][j] = f[i - 1][j] + f[i][j - 1]
        return f[m - 1][n - 1]


class _2nd:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        f = [0] * n
        f[0] = 0 if grid[0][0] == 1 else 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    f[j] = 0
                    continue
                if (j - 1) >= 0 and grid[i][j - 1] == 0:
                    f[j] += f[j - 1]
        return f[n - 1]


class _3rd:
    print("")


class _4th:
    print("")


if __name__ == '__main__':
    handlers = [_1st(), _2nd()]
    for handler in handlers:
        handler.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
