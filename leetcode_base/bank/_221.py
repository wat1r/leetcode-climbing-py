from typing import List


class _1st:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        f = [[0] * n for _ in range(m)]
        width = 0
        for i in range(m):
            for j in range(n):
                f[i][j] = 1 if matrix[i][j] == "1" else 0
                width = max(width, f[i][j])
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == "1":
                    f[i][j] = min(f[i - 1][j], f[i - 1][j - 1], f[i][j - 1]) + 1
                    width = max(width, f[i][j])
        return width * width


class _2nd:
    print("")


class _3rd:
    print("")


class _4th:
    print("")


if __name__ == '__main__':
    handlers = [_1st()]
    for handler in handlers:
        print("")
