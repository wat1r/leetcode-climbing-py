from typing import List


class _1st:
    # WA
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        f = [[0] * (n) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    f[i][j] = grid[0][0]
                #  i-1 或者 j-1 等于0时，不报错，值为0
                elif i == 0 or j == 0:
                    f[i][j] = grid[i][j] + f[i - 1][j - 1]
                else:
                    f[i][j] = grid[i][j] + min(f[i - 1][j], f[i][j - 1])
        print(f)
        return f[m - 1][n - 1]


class _2nd:
    # AC
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        f = [[0] * (n) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    f[i][j] = grid[0][0]
                elif i == 0:
                    f[i][j] = grid[i][j] + f[0][j - 1]
                elif j == 0:
                    f[i][j] = grid[i][j] + f[i - 1][0]
                else:
                    f[i][j] = grid[i][j] + min(f[i - 1][j], f[i][j - 1])
        print(f)
        return f[m - 1][n - 1]


class _3rd:
    print("")


class _4th:
    print("")


if __name__ == '__main__':
    handlers = [_1st(), _2nd()]
    for handler in handlers:
        h = handler
        h.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]])
    # handler.minPathSum([[1, 2, 3], [4, 5, 6]])
