from typing import List


class _1st:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        f = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            f[i][0] = f[i - 1][0] + ord(s1[i - 1])
            for j in range(1, n + 1):
                f[0][j] = f[0][j - 1] + ord(s2[j - 1])
                if s1[i - 1] == s2[j - 1]:
                    f[i][j] = f[i - 1][j - 1]
                else:
                    f[i][j] = min(f[i - 1][j] + ord(s1[i - 1]), f[i][j - 1] + ord(s2[j - 1]))
        return f[m][n]


class _2nd:
    # 反着求，求最长公共子序列
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        f = [[0] * (n + 1) for _ in range(m + 1)]  # 最长公共子序列的asc值
        total = 0
        for x in s1:
            total += ord(x)
        for y in s2:
            total += ord(y)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    f[i][j] = f[i - 1][j - 1] + ord(s1[i - 1]) + ord(s2[j - 1])
                else:
                    f[i][j] = max(f[i - 1][j], f[i][j - 1])
        return total - f[m][n]


class _3rd:
    print("")


class _4th:
    print("")


if __name__ == '__main__':
    handler = _1st()
