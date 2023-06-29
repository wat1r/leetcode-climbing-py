from typing import List


class _1st:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        f = [0] * (n + 1)
        f[0] = 0
        f[1] = 1
        for i in range(2, n + 1):
            f[i] = f[i - 1] + f[i - 2]
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
        handler.fib(2)
