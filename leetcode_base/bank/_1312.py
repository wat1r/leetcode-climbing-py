from typing import List


class _1st:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        t = s[::-1]
        f = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                f[i][j] = max(f[i - 1][j], f[i][j - 1])
                if s[i - 1] == t[j - 1]:
                    f[i][j] = max(f[i][j], f[i - 1][j - 1] + 1)
        return n - f[n][n]


class _2nd:
    print("")


class _3rd:
    print("")


class _4th:
    print("")


if __name__ == '__main__':
    handler = _1st
