from typing import List


class _1st:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        f = [0] * (n + 1)
        f[1] = f[2] = 1
        for i in range(3, n + 1):
            f[i] = f[i - 1] + f[i - 2] + f[i - 3]
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
        print("")
