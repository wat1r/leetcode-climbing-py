from linecache import cache


class _1st:
    def minDistance(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        @cache
        def dfs(i, j):
            if i < 0:
                return j + 1
            if j < 0:
                return i + 1;
            if s[i] == t[j]:
                return dfs(i - 1, j - 1)
            else:
                return min(dfs(i - 1, j), dfs(i, j - 1), dfs(i - 1, j - 1)) + 1

        return dfs(m - 1, n - 1)


class _2nd:
    def minDistance(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        f = [[0] * (n + 1) for _ in range(m + 1)]
        f[0] = list(range(n + 1))
        for i, x in enumerate(s):
            f[i + 1][0] = i + 1
            for j, y in enumerate(t):
                f[i + 1][j + 1] = f[i][j] if x == y else min(f[i][j + 1], f[i + 1][j], f[i][j]) + 1
        return f[m][n]


class _3rd:
    print("")


class _4th:
    print("")


if __name__ == '__main__':
    handler = _2nd()
    handler.minDistance("horse","ros")