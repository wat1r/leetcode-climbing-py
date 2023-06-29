from typing import List


class _1st:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n:
            return 0
        f = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            f[i][n] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == t[j]:
                    f[i][j] = f[i + 1][j + 1] + f[i + 1][j]
                else:
                    f[i][j] = f[i + 1][j]
        return f[0][0]


class _2nd:
    # 正着求解
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n:
            return 0
        f = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            f[i][0] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    f[i][j] = f[i - 1][j - 1] + f[i - 1][j]
                else:
                    f[i][j] = f[i - 1][j]
        return f[m][n]


class _3rd:
    # 正着求解
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n:
            return 0
        f = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            f[i][0] = 1
        for i in range(0, m):
            for j in range(0, n):
                if s[i] == t[j]:
                    f[i + 1][j + 1] = f[i][j] + f[i][j + 1]
                else:
                    f[i + 1][j + 1] = f[i][j + 1]
        return f[m][n]


class _4th:
    print("")


if __name__ == '__main__':
    handler = _1st()
