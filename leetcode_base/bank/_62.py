from typing import List


class _1st:
    def uniquePaths(self, m: int, n: int) -> int:
        f = [[0] * n for _ in range(m)]
        for i in range(m):
            f[i][0] = 1
        for j in range(n):
            f[0][j] = 1
        for i in range(m - 1):
            for j in range(n - 1):
                f[i + 1][j + 1] = f[i + 1][j] + f[i][j + 1]
        return f[m - 1][n - 1]


class _2nd:
    def uniquePaths(self, m: int, n: int) -> int:
        f = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = f[i - 1][j] + f[i][j - 1]
        return f[m - 1][n - 1]


class _3rd:
    def uniquePaths(self, m: int, n: int) -> int:
        f = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    f[i][j] = 1
                else:
                    f[i][j] = f[i - 1][j] + f[i][j - 1]
        return f[m - 1][n - 1]


class _4th:
    print("")


if __name__ == '__main__':
    handler = _1st()
    handler = _2nd()
    handler.uniquePaths(3, 7)
