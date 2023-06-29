from typing import List


class _1st:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        f = [0] * (n + 1)
        f[1] = 1
        f[2] = 2
        for i in range(3, n + 1):
            f[i] = f[i - 1] + f[i - 2]
        return f[n]


class _2nd:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        f = [0] * n
        f[0] = 1
        f[1] = 2
        for i in range(2, n):
            f[i] = f[i - 1] + f[i - 2]
        return f[n-1]


class _3rd:
    print("")


class _4th:
    print("")


if __name__ == '__main__':
    handlers = [_1st()]
    for handler in handlers:
        handler.climbStairs(3)
