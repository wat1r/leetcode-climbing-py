from cmath import inf
from typing import List


class _1st:
    def numSquares(self, n: int) -> int:
        f = [inf] * (n + 1)
        f[0] = 0
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if j * j > n:
                    break
                f[i] = min(f[i], f[i - j * j] + 1)
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
        handler.numSquares(12)
