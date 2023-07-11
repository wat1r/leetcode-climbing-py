from typing import List


class _1st:
    def mostPoints(self, q: List[List[int]]) -> int:
        n = len(q)
        f = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            f[i] = max(f[i + 1], q[i][0] + f[min(n, i + q[i][1] + 1)])
        return f[0]


class _2nd:
    def mostPoints(self, q: List[List[int]]) -> int:
        n = len(q)
        f = [0] * (n + 1)
        for i, (point, brainpower) in enumerate(q):
            f[i + 1] = max(f[i + 1], f[i])
            j = min(n, i + brainpower + 1)
            f[j] = max(f[j], f[i] + point)
        return f[n]


class _3rd:
    print("")


class _4th:
    print("")


if __name__ == '__main__':
    handlers = [_1st(), _2nd()]
    for handler in handlers:
        handler.mostPoints([[3, 2], [4, 3], [4, 4], [2, 5]])
