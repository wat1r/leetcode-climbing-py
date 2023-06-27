from linecache import cache


class _1st:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[m][n]


class _2nd:
    def longestCommonSubsequence(self, s: str, t: str) -> int:
        m, n = len(s), len(t)

        @cache
        def dfs(i, j):
            if i < 0 or j < 0:
                return 0
            if s[i] == t[j]:
                return dfs(i - 1, j - 1) + 1
            else:
                return max(dfs(i - 1, j), dfs(i, j - 1))

        return dfs(m - 1, n - 1)


class _3rd:
    def longestCommonSubsequence(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        f = [[0] * (n + 1) for _ in range(m + 1)]
        for i, x in enumerate(s):
            for j, y in enumerate(t):
                # if x == y:
                #     f[i + 1][j + 1] = f[i][j] + 1
                # else:
                #     f[i + 1][j + 1] = max(f[i][j + 1], f[i + 1][j])
                f[i + 1][j + 1] = f[i][j] + 1 if x == y else max(f[i][j + 1], f[i + 1][j])
        return f[m][n]


class _4th:
    def longestCommonSubsequence(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        f = [0] * (n + 1)
        for i, x in enumerate(s):
            pre = f[0]  # 0
            for j, y in enumerate(t):
                tmp = f[j + 1]
                f[j + 1] = pre + 1 if x == y else max(f[j + 1], f[j])
                pre = tmp
        return f[n]
