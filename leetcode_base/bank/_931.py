from cmath import inf
from typing import List


class _1st:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        f = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                f[0][j] = matrix[0][j]
                if i > 0:
                    f[i][j] = min(f[i - 1][j - 1] if j > 0 else inf
                                  , f[i - 1][j],
                                  f[i - 1][j + 1] if j < n - 1 else inf) + matrix[i][j]
        return min(f[n - 1])


class _2nd:
    print("")


class _3rd:
    print("")


class _4th:
    print("")


if __name__ == '__main__':
    handlers = [_1st()]
    for handler in handlers:
        handler.minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]])
