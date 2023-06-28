from typing import List


class _1st:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        f = [False for _ in range(n + 1)]
        f[0] = True
        for i in range(n + 1):
            for j in range(i):
                if f[j] and wordDict.count(s[j:i]) > 0:
                    f[i] = True
                    break
        return f[n]


class _2nd:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        f = [False for _ in range(n + 1)]
        f[0] = True
        for i in range(n + 1):
            for j in range(i):
                if f[j] and s[j:i] in wordDict:
                    f[i] = True
                    break
        return f[n]


class _3rd:
    print("")


class _4th:
    print("")


if __name__ == '__main__':
    handler = _1st()
    handler.wordBreak("leetcode", ["leet", "code"])
