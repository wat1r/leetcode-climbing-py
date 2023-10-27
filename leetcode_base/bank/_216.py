from typing import List


class _1st:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        path = []

        def dfs(i: int, t: int):
            d = k - len(path)
            if t < 0 or t > (i + i - d + 1) * d // 2:
                return
            if len(path) == k:
                ans.append(path.copy())
                return
            for j in range(i, d - 1, -1):
                path.append(j)
                dfs(j - 1, t - j)
                path.pop()

        dfs(9, n)
        print(ans)
        return ans


class _2nd:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        path = []

        def dfs(i: int, t: int):
            d = k - len(path)
            if t < 0 or t > (i + i - d + 1) * d // 2:
                return
            if len(path) == k:
                ans.append(path.copy())
                return
            if i > d:
                dfs(i - 1, t)
            path.append(i)
            dfs(i - 1, t - i)
            path.pop()

        dfs(9, n)
        # print(ans)
        return ans


class _3rd:
    print("")


class _4th:
    print("")


if __name__ == '__main__':
    handlers = [_1st()]
    for handler in handlers:
        k, n = 3, 7
        handler.combinationSum3(k, n)
