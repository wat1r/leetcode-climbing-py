from cmath import inf
from linecache import cache
from typing import List


class _1st:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)

        @cache
        def dfs(i, j):
            if i < 0:
                return -inf
            if j == 0:
                return max(dfs(i - 1, 0), 0) + arr[i]
            return max(dfs(i - 1, 1) + arr[i], dfs(i - 1, 0))

        return max(max(dfs(k, 0), dfs(k, 1)) for k in range(0, n))


class _2nd:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        f = [[-inf] * 2] + [[0] * 2 for _ in range(n)]
        for i, x in enumerate(arr):
            f[i + 1][0] = max(f[i][0], 0) + x
            f[i + 1][1] = max(f[i][1] + x, f[i][0])
        # for v in f:
        #     print(v)
        return max(max(v) for v in f)


class _3rd:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        f0 = f1 = res = -inf
        # for x in enumerate(arr):
        for x in arr:
            f1 = max(f1 + x, f0)
            f0 = max(f0, 0) + x
            res = max(res, f0, f1)
        return res


class _4th:
    print("")


if __name__ == '__main__':
    # handler = _2nd()
    handler = _3rd()
    arr = [1, -2, 0, 3]
    handler.maximumSum(arr)
