from linecache import cache
from math import inf
from typing import List


class _1st:
    def minScoreTriangulation(self, v: List[int]) -> int:
        n = len(v)

        @cache
        def dfs(i, j):
            if i + 1 == j:
                return 0
            res = inf
            for k in range(i + 1, j):
                res = min(res, dfs(i, k) + dfs(k, j) + v[i] * v[k] * v[j])
            return res

        return dfs(0, n - 1)


class _2nd:
    print("")


class _3rd:
    print("")


class _4th:
    print("")
