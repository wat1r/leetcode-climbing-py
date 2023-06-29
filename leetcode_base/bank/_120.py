from cmath import inf
from typing import List


class _1st:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        f = [[0] * n for _ in range(n)]
        f[0][0] = triangle[0][0]
        for i in range(1, n):
            f[i][0] = f[i - 1][0] + triangle[i][0]
            for j in range(1, i):
                f[i][j] = min(f[i - 1][j], f[i - 1][j - 1]) + triangle[i][j]
            f[i][i] = f[i - 1][i - 1] + triangle[i][i]
        return min(f[n - 1])


class _2nd:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        f = [[0] * n for _ in range(n)]
        f[0][0] = triangle[0][0]
        for i in range(1, n):
            f[i][0] = f[i - 1][0] + triangle[i][0]
            for j in range(1, i + 1):
                f[i][j] = min(inf if j == i else f[i - 1][j], f[i - 1][j - 1]) + triangle[i][j]
            # f[i][i] = f[i - 1][i - 1] + triangle[i][i]
        return min(f[n - 1])


class _3rd:
    print("")


class _4th:
    print("")


if __name__ == '__main__':
    handlers = [_1st(), _2nd()]
    for handler in handlers:
        handler.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])
