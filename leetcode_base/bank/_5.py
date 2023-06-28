from typing import List


class _1st:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        maxLen = 0
        f = [[False] * n for _ in range(n)]
        res = ""
        for j in range(n):
            for i in range(j + 1):
                if s[i] == s[j] and ((j - i) <= 2 or f[i + 1][j - 1]):
                    f[i][j] = True
                if f[i][j] and j - i + 1 > maxLen:
                    maxLen = j - i + 1
                    res = s[i:j + 1]
        return res


class _2nd:
    print("")


class _3rd:
    print("")


class _4th:
    print("")


if __name__ == '__main__':
    handler = _1st()
    handler.longestPalindrome("cbbd")
